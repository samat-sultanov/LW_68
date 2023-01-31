async function makeRequest(url, method = 'GET') {
    let response = await fetch(url, {method});

    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

function onError(error) {
    console.log(error);
}

async function ArticleAddLike(event) {
    event.preventDefault();
    let target = event.target;
    let url = target.href;
    try {
        let response = await makeRequest(url);
        let articleId = target.dataset.articleId;
        let text = document.getElementById(articleId);
        if (text.innerText === "Dislike") {
            text.innerText = "Like";
        } else {
            text.innerText = "Dislike";
        }
        let art_like_count = response.art_like_count;
        let p = document.getElementById('article_likes_total');
        p.innerText = `Total likes ${art_like_count}`;
    } catch (error) {
        onError(error);
    }
}

async function CommentAddLike(event) {
    event.preventDefault();
    let target = event.target;
    let url = target.href;
    try {
        let response = await makeRequest(url);
        let commentId = target.dataset.commentId;
        let text = document.getElementById(commentId);
        if (text.innerText === "Dislike") {
            text.innerText = "Like";
        } else {
            text.innerText = "Dislike";
        }
        let comm_like_count = response.comm_like_count;
        let p = document.getElementById('comment_likes_total');
        p.innerText = `Total likes ${comm_like_count}`;
    } catch (error) {
        onError(error);
    }
}

async function onloadFunc() {
    let likes = document.getElementsByClassName("btn likes");
    for (let i = 0; i < likes.length; i++) {
        likes[i].addEventListener("click", ArticleAddLike);
    }

    let like = document.getElementsByClassName("btn likes comment");
    for (let i = 0; i < like.length; i++) {
        like[i].addEventListener("click", CommentAddLike);
    }
}

window.addEventListener("load", onloadFunc);