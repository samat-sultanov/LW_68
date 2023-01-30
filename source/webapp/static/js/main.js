    async function buttonClick(event) {
        let target = event.target;
        let url = target.dataset['indexLink'];
        let response = await fetch(url);
        if(response.ok) {
            console.log('200 ok');
        } else if (response.status === 400){
            console.log('400');
        }
        let index_text = await response.json();
        console.log(index_text);
    }

    async function onLoad(){
        let button = document.getElementById('button');
        if (button){
            button.onclick = buttonClick;
        }

    }

    window.addEventListener('load', onLoad)