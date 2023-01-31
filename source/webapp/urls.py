from django.urls import path
from webapp.views import IndexViews, ArticleCreateView, ArticleView, ArticleUpdateView, \
    ArticleDeleteView, ArticleCommentCreateView, CommentUpdateView, CommentDeleteView, ArticleLikeView, CommentLikeView

app_name = 'webapp'

urlpatterns = [
    path('', IndexViews.as_view(), name='index'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article_view'),
    path('article/<int:pk>/comment/add/', ArticleCommentCreateView.as_view(), name='article_comment_add'),
    path('articles/add/', ArticleCreateView.as_view(), name='article_add'),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
    path('comment/<int:pk>/update', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment_delete'),
    path("article/<int:pk>/like", ArticleLikeView.as_view(), name="likes"),
    path("comment/<int:pk>/like", CommentLikeView.as_view(), name="comment_likes"),
]
