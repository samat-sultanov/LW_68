from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.http import urlencode
from webapp.models import Article, Comment
from webapp.forms import ArticleForm, SimpleSearchForm, ArticleDeleteForm
from django.http import JsonResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View


class ArticleLikeView(LoginRequiredMixin, View):
    def get(self, request, *args, pk, **kwargs):
        article = Article.objects.get(pk=pk)
        user = self.request.user

        if user in article.likes.all():
            article.likes.remove(user)
        else:
            article.likes.add(user)

        return JsonResponse({"art_like_count": article.likes.count()})


class CommentLikeView(LoginRequiredMixin, View):
    def get(self, request, *args, pk, **kwargs):
        comment = Comment.objects.get(pk=pk)
        user = self.request.user

        if user in comment.like.all():
            comment.like.remove(user)
        else:
            comment.like.add(user)

        return JsonResponse({"comm_like_count": comment.like.count()})


class IndexViews(ListView):
    template_name = 'article/index.html'
    context_object_name = 'articles'
    model = Article
    ordering = ('-created_at',)
    paginate_by = 3
    paginate_orphans = 2

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(title__icontains=self.search_value) | Q(author__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class ArticleView(DetailView):
    template_name = 'article/article_view.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object
        comments = article.comments.order_by('-created_at')
        context['comments'] = comments
        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article/article_create.html"
    model = Article
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = "article/article_update.html"
    form_class = ArticleForm
    model = Article
    context_object_name = 'article'
    permission_required = 'webapp.change_article'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    # def has_permission(self):
    #     project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
    #     return super().has_permission() and self.request.user in project.user.all()


class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'article/article_delete.html'
    model = Article
    context_object_name = 'article'
    success_url = reverse_lazy('index')
    form_class = ArticleDeleteForm
    permission_required = 'webapp.delete_article'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
