// $(document).ready(function(){
// $('.like-form').submit(function(event){
//                 event.preventDefault()
//                 const article_id = $(this).attr('id')
//                 const likeText = $(`.like-btn${article_id}`).text()
//                 const trim = $.trim(likeText)
//                 const url = $(this).attr('action')
//
//                 let res;
//                 const likes = $(`.like-count${article_id}`).text()
//                 const trimCount = parseInt(likes)
//
//                 $.ajax({
//                     type: 'POST',
//                     url: url,
//                     data: {
//                         'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
//                         'article_id':article_id,
//                     },
//                     success: function(response) {
//                         if(trim === 'Unlike') {
//                             $(`.like-btn${article_id}`).text('Like')
//                             res = trimCount - 1
//                         } else {
//                             $(`.like-btn${article_id}`).text('Unlike')
//                             res = trimCount + 1
//                         }
//                         $(`.like-count${article_id}`).text(res)
//                     },
//                     error: function(response) {
//                         console.log('error', response)
//                     }
//                 })
//             })
// });
