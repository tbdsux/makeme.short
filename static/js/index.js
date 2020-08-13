// durect shorten link modal
const openShortenModal = document.getElementById('open-ShortenModal');
const closeShortenModal = document.getElementById('close-ShortenModal');
const shortenModal = document.getElementById('directShorten-modal');
const shortenModalContainer = document.getElementById('directShorten-container');

openShortenModal.onclick = function(){
    shortenModal.classList.remove('hidden');
}
closeShortenModal.onclick = function(){
    shortenModal.classList.add('hidden');
}
shortenModal.onclick = function(e){
    if (e.target != shortenModalContainer){
        if (!shortenModalContainer.contains(e.target)){
            shortenModal.classList.add('hidden');
        }
    }
}

// mobile navigation
const btnMobilenav = document.getElementById('toggle-nav');
const mainNav = document.getElementById('main-nav');

btnMobilenav.onclick = function(){
    mainNav.classList.toggle('hidden');
}

// direct shorten modal
const inputDirectUrl = document.getElementById('input-urlDirect');
const btnDirectShorten = document.getElementById('btn-shortenDirecturl');
const errorContainer = document.getElementById('url-error');

function checkUrl(){
    if (inputDirectUrl.value.length > 0){
        if (validateUrl(inputDirectUrl.value) == true){
            // hide the error
            errorContainer.classList.add('hidden');
            // show correct url style
            inputDirectUrl.classList.add('border-med-turq');
            inputDirectUrl.classList.add('text-midnight-green');
            inputDirectUrl.classList.remove('border-red-600');
            inputDirectUrl.classList.remove('text-red-600');
            // enable the shorten button
            btnDirectShorten.disabled = false;
            btnDirectShorten.classList.remove('opacity-75');
            btnDirectShorten.classList.remove('cursor-not-allowed');
            btnDirectShorten.classList.add('cursor-pointer');
            btnDirectShorten.classList.add('hover:bg-midnight-green');
            btnDirectShorten.classList.add('hover:text-white');
        }
        else{
            // show the error
            errorContainer.classList.remove('hidden');
            // show error border
            inputDirectUrl.classList.remove('border-med-turq');
            inputDirectUrl.classList.remove('text-midnight-green');
            inputDirectUrl.classList.add('border-red-600');
            inputDirectUrl.classList.add('text-red-600');
            // disable the shorten button
            btnDirectShorten.disabled = true;
            btnDirectShorten.classList.add('opacity-75');
            btnDirectShorten.classList.add('cursor-not-allowed');
            btnDirectShorten.classList.remove('cursor-pointer');
            btnDirectShorten.classList.remove('hover:bg-midnight-green');
            btnDirectShorten.classList.remove('hover:text-white');
        }
    }
    else{
        // hide the error
        errorContainer.classList.add('hidden');
        // set back to normal
        inputDirectUrl.classList.remove('border-med-turq');
        inputDirectUrl.classList.remove('text-midnight-green');
        inputDirectUrl.classList.remove('border-red-600');
        inputDirectUrl.classList.remove('text-red-600');
        // disable the shorten button
        btnDirectShorten.disabled = true;
        btnDirectShorten.classList.add('opacity-75');
        btnDirectShorten.classList.add('cursor-not-allowed');
        btnDirectShorten.classList.remove('cursor-pointer');
        btnDirectShorten.classList.remove('hover:text-napples-yellow');
        btnDirectShorten.classList.remove('hover:text-white');
    }
}

inputDirectUrl.oninput = function(){
    checkUrl();
}

// get url from main to the modal
const toModalUrl = document.getElementById('modal-urlinput');
toModalUrl.oninput = function(){
    inputDirectUrl.value = toModalUrl.value;
    checkUrl();
}

function validateUrl(url){
    const urlFormat = /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)/;
    if (urlFormat.test(url) == true){
        return true;
    }
    return false;
}


// on window load
window.onload = function(){
    btnDirectShorten.disabled = true;
}