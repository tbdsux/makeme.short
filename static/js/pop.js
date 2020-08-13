// shortenModal
const shortenModal = document.getElementById('shortenModal');
const shortenModalContainer = document.getElementById('shortenModal-container');
const closeShortenModal = document.getElementById('close-shortenModal');
const openShortenModal = document.getElementById('open-shortenModal');

closeShortenModal.onclick = function(){
    hideModal();
}
openShortenModal.onclick = function(){
    showModal();
}
shortenModal.onclick = function(e){
    if (e.target != shortenModalContainer){
        if (!shortenModalContainer.contains(e.target)){
            hideModal();
        }
    }
}

function hideModal(){
    shortenModal.classList.add('hidden');
}
function showModal(){
    shortenModal.classList.remove('hidden');
}

// sidenav
const sidenav = document.getElementById('sidenav');
const sidenavContainer = document.getElementById('sidenav-container');
const closeSidenav = document.getElementById('close-sidenav');
const openSidenav = document.getElementById('open-sidenav');

closeSidenav.onclick = function(){
    hideSidenav();
}
openSidenav.onclick = function(){
    showSidenav();
}
sidenav.onclick = function(e){
    if (e.target != sidenavContainer){
        if (!sidenavContainer.contains(e.target)){
            hideSidenav();
        }
    }
}

function showSidenav(){
    sidenav.classList.remove('hidden');
}
function hideSidenav(){
    sidenav.classList.add('hidden');
}

// update account settings
const formUserInfo = document.getElementById('form-userInfo');
const formUserPass = document.getElementById(('form-userPass'));
const btnFormUserInfo = document.getElementById('btn-formUserInfo');
const btnFormUserPass = document.getElementById('btn-formUserPass');

const activeFormTab = ['text-napples-yellow', 'border-none'];
const inactiveFormTab = ['border']; 

btnFormUserInfo.onclick = function(){
    formUserInfo.classList.remove('hidden');
    btnFormUserInfo.classList.remove(...inactiveFormTab);
    btnFormUserInfo.classList.add(...activeFormTab);
    formUserPass.classList.add('hidden');
    btnFormUserPass.classList.add(...inactiveFormTab);
    btnFormUserPass.classList.remove(...activeFormTab);
}
btnFormUserPass.onclick = function(){
    formUserInfo.classList.add('hidden');
    btnFormUserInfo.classList.add(...inactiveFormTab);
    btnFormUserInfo.classList.remove(...activeFormTab);
    formUserPass.classList.remove('hidden');
    btnFormUserPass.classList.remove(...inactiveFormTab);
    btnFormUserPass.classList.add(...activeFormTab);
}

// when the window resizes
window.onresize = function(){
    if (screen.width >= 768){
        showSidenav();
    }
}