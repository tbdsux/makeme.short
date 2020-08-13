// shorten new url modal
const enabtnShorten = ['cursor-pointer', 'bg-napples-yellow', 'hover:opacity-100'];
const disbtnShorten = ['cursor-not-allowed', 'bg-gray-400'];

const inputUrl = document.getElementById('input-url');
const inputUrlDesc = document.getElementById('input-url-desc');
const btnShorten = document.getElementById('btn-shorten');

inputUrl.oninput = function(){
    if (inputUrl.value.length > 0){
        if (validateUrl(inputUrl.value) == true){
            btnShorten.disabled = false;
            btnShorten.classList.remove(...disbtnShorten);
            btnShorten.classList.add(...enabtnShorten);
            showValid(inputUrl);
        }
        else{
            showError(inputUrl, 'Invalid URL!')
        }
    }
    else{
        showNormal(inputUrl);
        btnShorten.disabled = true;
        btnShorten.classList.add(...disbtnShorten);
        btnShorten.classList.remove(...enabtnShorten);
    }
}
inputUrlDesc.oninput = function(){
    if (inputUrlDesc.value.length > 0){
        showValid(inputUrlDesc);
        if ((inputUrl.value.length > 0) && (validateUrl(inputUrl.value) == true)){
            btnShorten.disabled = false;
            btnShorten.classList.remove(...disbtnShorten);
            btnShorten.classList.add(...enabtnShorten);
        }
        else{
            btnShorten.disabled = true;
            btnShorten.classList.add(...disbtnShorten);
            btnShorten.classList.remove(...enabtnShorten);
        }
    }
    else{
        showNormal(inputUrlDesc);
    }
}


function validateUrl(url){
    const urlFormat = /^(?:(?:(?:https?|ftp):)?\/\/)(?:\S+(?::\S*)?@)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z0-9\u00a1-\uffff][a-z0-9\u00a1-\uffff_-]{0,62})?[a-z0-9\u00a1-\uffff]\.)+(?:[a-z\u00a1-\uffff]{2,}\.?))(?::\d{2,5})?(?:[/?#]\S*)?$/i;
    if (urlFormat.test(url) == true){
        return true;
    }
    return false;
}


// button variables
const disBtnUpdate = ['opacity-75', 'cursor-not-allowed'];
const enaBtnUpdate = ['opacity-100', 'cursor-pointer', 'hover:bg-napples-yellow']

// update user info
const btnUpUser = document.getElementById('btnUp-user');
const inputProfileImg = document.getElementById('update-profileimg');
const inputUsername = document.getElementById('update-username');
const inputEmail = document.getElementById('update-email');

let currentUsername;
let currentEmail;

inputProfileImg.onchange = function(){
    if (inputProfileImg.value.length > 0){
        btnUpUser.disabled = false;
        btnUpUser.classList.remove(...disBtnUpdate);
        btnUpUser.classList.add(...enaBtnUpdate);
    }
    else{
        if ((inputProfileImg.value.length == 0) && (inputUsername.value.length == 0) && (inputEmail.value.length == 0)){
            btnUpUser.disabled = true;
            btnUpUser.classList.add(...disBtnUpdate);
            btnUpUser.classList.remove(...enaBtnUpdate);
        }
    }
}

inputUsername.oninput = function(){
    if ((inputUsername.value.length > 2) && (inputUsername.value != currentUsername)){
        if (validateUsername(inputUsername.value) == true){
            showValid(inputUsername);
            btnUpUser.disabled = false;
            btnUpUser.classList.remove(...disBtnUpdate);
            btnUpUser.classList.add(...enaBtnUpdate);
        }
        else{
            showError(inputUsername, 'Blank spacces not allowed.')
        }
    }
    else if ((inputUsername.value.length == 0) || (inputUsername.value == currentUsername)){
        showNormal(inputUsername);
        inputUsername.value = currentUsername;
        btnUpUser.disabled = true;
        btnUpUser.classList.add(...disBtnUpdate);
        btnUpUser.classList.remove(...enaBtnUpdate);
    }
    else{
        showError(inputUsername, 'Username is too short!');
        if ((inputProfileImg.value.length == 0) && (inputUsername.value.length == 0) && (inputUsername.value == currentUsername) && (inputEmail.value.length == 0) && (inputEmail.value == currentEmail)){
            btnUpUser.disabled = true;
            btnUpUser.classList.add(...disBtnUpdate);
            btnUpUser.classList.remove(...enaBtnUpdate);
        }
    }
}

inputEmail.oninput = function(){
    if ((inputEmail.value.length > 0) && (inputEmail.value != currentEmail)){
        if (validateEmail(inputEmail.value) == true){
            showValid(inputEmail);
            btnUpUser.disabled = false;
            btnUpUser.classList.remove(...disBtnUpdate);
            btnUpUser.classList.add(...enaBtnUpdate);
        }
        else{
            showError(inputEmail, 'Invalid email address!')
        }
    }
    else if ((inputEmail.value.length == 0) || (inputEmail.value == currentEmail)){
        showNormal(inputEmail);
        inputEmail.value = currentEmail;
        btnUpUser.disabled = true;
        btnUpUser.classList.add(...disBtnUpdate);
        btnUpUser.classList.remove(...enaBtnUpdate);
    }
    else{
        showError(inputEmail, 'Username is too short!');
        if ((inputProfileImg.value.length == 0) && (inputUsername.value.length == 0) && (inputUsername.value == currentUsername) && (inputEmail.value.length == 0) && (inputEmail.value == currentEmail)){
            btnUpUser.disabled = true;
            btnUpUser.classList.add(...disBtnUpdate);
            btnUpUser.classList.remove(...enaBtnUpdate);
        }
    }
}

function validateUsername(uname){
    const unameFormat = /^\S*$/;
    if (uname.match(unameFormat)){
        return true;
    }
    
    return false;
}

// for email validation
function validateEmail(email){
    const mailFormat = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (mailFormat.test(email)){
        return true;
    }
    
    return false;
}


// update password
const btnUpPassword = document.getElementById('btnUp-password');
const inputPassword = document.getElementById('update-password');
const inputConPassword = document.getElementById('update-con-password');

inputPassword.oninput = function(){
    if ((inputPassword.value.length > 7) && (inputPassword.value.length != 0)){
        showValid(inputPassword);
        if ((inputPassword.value.length > 7) && (inputConPassword.value == inputPassword.value)){
            btnUpPassword.disabled = false;
            btnUpPassword.classList.remove(...disBtnUpdate);
            btnUpPassword.classList.add(...enaBtnUpdate);
        }
        else{
            btnUpPassword.disabled = true;
            btnUpPassword.classList.add(...disBtnUpdate);
            btnUpPassword.classList.remove(...enaBtnUpdate);
        }
    }
    else{
        if (inputPassword.value.length != 0){
            showError(inputPassword, 'Password is too short!')
        }
        else{
            showNormal(inputPassword);
            btnUpPassword.disabled = true;
            btnUpPassword.classList.add(...disBtnUpdate);
            btnUpPassword.classList.remove(...enaBtnUpdate);
        }
    }
}
inputConPassword.oninput = function(){
    if ((inputConPassword.value == inputPassword.value) && (inputConPassword.value.length > 7)){
        showValid(inputConPassword);
        if ((inputPassword.value.length > 7) && (inputConPassword.value == inputPassword.value)){
            btnUpPassword.disabled = false;
            btnUpPassword.classList.remove(...disBtnUpdate);
            btnUpPassword.classList.add(...enaBtnUpdate);
        }
        else{
            btnUpPassword.disabled = true;
            btnUpPassword.classList.add(...disBtnUpdate);
            btnUpPassword.classList.remove(...enaBtnUpdate);
        }
    }
    else{
        if (inputConPassword.value.length != 0){
            showError(inputConPassword, 'Passwords are not equal!')
        }
        else{
            showNormal(inputConPassword);
            btnUpPassword.disabled = true;
            btnUpPassword.classList.add(...disBtnUpdate);
            btnUpPassword.classList.remove(...enaBtnUpdate);
        }
    }
}

// show error function
function showError(tb, errMessage){
    const inputContainer = (tb.parentElement).parentElement;
    const errorContainer = inputContainer.querySelector('.error');
    const errMsgContainer = inputContainer.querySelector('p');
    const errIcon = inputContainer.querySelector('#icError');
    const valIcon = inputContainer.querySelector('#icCheck');
    const inputIcon = inputContainer.querySelector('#input-icon');
    
    tb.classList.add('border-red-600');
    tb.classList.remove('focus:border-med-turq');
    tb.classList.add('text-red-600');
    tb.classList.remove('border-med-turq');
    tb.classList.remove('text-midnight-green');
    errorContainer.classList.remove('hidden'); // show the error
    errMsgContainer.innerText = errMessage; // replace error message
    inputIcon.classList.remove('text-med-turq');
    inputIcon.classList.remove('text-gray-500');
    inputIcon.classList.add('text-red-600');
    errIcon.classList.remove('invisible'); // show error icon
    valIcon.classList.add('invisible'); // hide the check icon
}
// show correct input function
function showValid(tb){
    const inputContainer = (tb.parentElement).parentElement;
    const errorContainer = inputContainer.querySelector('.error');
    const errIcon = inputContainer.querySelector('#icError');
    const valIcon = inputContainer.querySelector('#icCheck');
    const inputIcon = inputContainer.querySelector('#input-icon');
    
    tb.classList.remove('border-red-600');
    tb.classList.add('focus:border-med-turq');
    tb.classList.remove('text-red-600');
    tb.classList.add('border-med-turq');
    tb.classList.add('text-midnight-green');
    errorContainer.classList.add('hidden'); // hide the error
    inputIcon.classList.add('text-med-turq');
    inputIcon.classList.remove('text-gray-500');
    inputIcon.classList.remove('text-red-600');
    errIcon.classList.add('invisible'); // hide error icon
    valIcon.classList.remove('invisible'); // show the check icon
}
// revert back to normal function
function showNormal(tb){
    const inputContainer = (tb.parentElement).parentElement;
    const errorContainer = inputContainer.querySelector('.error');
    const errIcon = inputContainer.querySelector('#icError');
    const valIcon = inputContainer.querySelector('#icCheck');
    const inputIcon = inputContainer.querySelector('#input-icon');
    
    tb.classList.remove('border-red-600');
    tb.classList.add('focus:border-med-turq');
    tb.classList.remove('text-red-600');
    tb.classList.remove('border-med-turq');
    tb.classList.remove('text-midnight-green');
    errorContainer.classList.add('hidden'); // hide the error
    inputIcon.classList.remove('text-med-turq');
    inputIcon.classList.add('text-gray-500');
    inputIcon.classList.remove('text-red-600');
    errIcon.classList.add('invisible'); // hide error icon
    valIcon.classList.add('invisible'); // show the check icon
}


// on window load
window.onload = function(){
    // disable the buttons
    btnUpUser.disabled = true;
    btnUpPassword.disabled = true;
    // get current values
    currentUsername = inputUsername.value;
    currentEmail = inputEmail.value;
    // disable the shorten url button
    btnShorten.disabled = true;
}