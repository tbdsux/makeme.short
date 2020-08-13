const ntTab = ['bg-napples-yellow', 'hover:bg-med-turq'];

var btnLogin = document.getElementById('loginTab');
var btnRegister = document.getElementById('registerTab');
var loginForm = document.getElementById('loginForm');
var registerForm = document.getElementById('registerForm');

//register button
btnRegister.onclick = function(){
    loginForm.classList.remove('block');
    loginForm.classList.add('hidden');
    registerForm.classList.add('block');
    registerForm.classList.remove('hidden');
    // switch css
    btnLogin.classList.remove('bg-white');
    btnLogin.classList.add(...ntTab);
    btnRegister.classList.remove(...ntTab);
    btnRegister.classList.add('bg-white');
}

//login button
btnLogin.onclick = function(){
    loginForm.classList.add('block');
    loginForm.classList.remove('hidden');
    registerForm.classList.remove('block');
    registerForm.classList.add('hidden');
    // switch css
    btnLogin.classList.add('bg-white');
    btnLogin.classList.remove(...ntTab);
    btnRegister.classList.add(...ntTab);
    btnRegister.classList.remove('bg-white');
}

// form validaation styles
const disableBtnForm = ['opacity-75', 'cursor-not-allowed'];
const enabledBtnForm = ['opacity-100', 'cursor-pointer', 'hover:bg-med-turq'];


// login form validation
const logUsername = document.getElementById('login-username');
const logPassword = document.getElementById('login-password');
const subLogin = document.getElementById('btn-login');

logUsername.oninput = function(){
    if (logUsername.value.length > 0 && logPassword.value.length > 0){
        subLogin.disabled = false;
        subLogin.classList.remove(...disableBtnForm);
        subLogin.classList.add(...enabledBtnForm);
    }else{
        subLogin.disabled = true;
        subLogin.classList.add(...disableBtnForm);
        subLogin.classList.remove(...enabledBtnForm);
    }
}

logPassword.oninput = function(){
    if (logUsername.value.length > 0 && logPassword.value.length > 0){
        subLogin.disabled = false;
        subLogin.classList.remove(...disableBtnForm);
        subLogin.classList.add(...enabledBtnForm);
    }else{
        subLogin.disabled = true;
        subLogin.classList.add(...disableBtnForm);
        subLogin.classList.remove(...enabledBtnForm);
    }
}


// register form validation
const regUsername = document.getElementById('register-username');
const regEmail = document.getElementById('register-email');
const regPassword = document.getElementById('register-password');
const regConPassword = document.getElementById('register-confirm-password');
const regAgreement = document.getElementById('check-register-agreement');
const subRegister = document.getElementById('btn-register');


regUsername.oninput = function(){
    if (regUsername.value.length > 0 ){
        if (regUsername.value.length >= 3){
            if (validateUsername(regUsername.value)){
                showValid(regUsername);
                if ((regUsername.value.length > 0) && (regEmail.value.length > 0) && (regPassword.value.length > 0) && (regConPassword.value === regPassword.value) && (regAgreement.checked === true)){
                    subRegister.disabled = false;
                    subRegister.classList.remove(...disableBtnForm);
                    subRegister.classList.add(...enabledBtnForm);
                }else{
                    subRegister.disabled = true;
                    subRegister.classList.add(...disableBtnForm);
                    subRegister.classList.remove(...enabledBtnForm);
                }
            }
            else{
                showError(regUsername, 'Username cannot contain blank spaces.')
            }
        }
        else{
            showError(regUsername, 'Username is too short.')
        }
    }
    else{
        showError(regUsername, 'Username cannot be blank.');
    }
    
}
regEmail.oninput = function(){
    if (regEmail.value.length > 0){
        if (validateEmail(regEmail.value) == true){
            showValid(regEmail);
            if ((regUsername.value.length > 0) && (regEmail.value.length > 0) && (regPassword.value.length > 0) && (regConPassword.value === regPassword.value) && (regAgreement.checked === true)){
                subRegister.disabled = false;
                subRegister.classList.remove(...disableBtnForm);
                subRegister.classList.add(...enabledBtnForm);
            }else{
                subRegister.disabled = true;
                subRegister.classList.add(...disableBtnForm);
                subRegister.classList.remove(...enabledBtnForm);
            }
        }
        else{
            showError(regEmail, 'Invalid email address.');
        }
    }
    else{
        showError(regEmail, 'Email cannot be blank.');
    }
    
}
regPassword.oninput = function(){
    if (regPassword.value.length > 0){
        showValid(regPassword);
        if ((regUsername.value.length > 0) && (regEmail.value.length > 0) && (regPassword.value.length > 0) && (regConPassword.value === regPassword.value) && (regAgreement.checked === true)){
            subRegister.disabled = false;
            subRegister.classList.remove(...disableBtnForm);
            subRegister.classList.add(...enabledBtnForm);
        }else{
            subRegister.disabled = true;
            subRegister.classList.add(...disableBtnForm);
            subRegister.classList.remove(...enabledBtnForm);
        }
    }
    else{
        showError(regPassword, 'Password cannot be blank.');
    }
}
regConPassword.oninput = function(){
    if (regConPassword.value === regPassword.value){
        showValid(regConPassword);
        if ((regUsername.value.length > 0) && (regEmail.value.length > 0) && (regPassword.value.length > 0) && (regConPassword.value === regPassword.value) && (regAgreement.checked === true)){
            subRegister.disabled = false;
            subRegister.classList.remove(...disableBtnForm);
            subRegister.classList.add(...enabledBtnForm);
        }else{
            subRegister.disabled = true;
            subRegister.classList.add(...disableBtnForm);
            subRegister.classList.remove(...enabledBtnForm);
        }
    }
    else{
        showError(regConPassword, 'Password not equal.');
    }
}
regAgreement.onclick = function(){
    if ((regUsername.value.length > 0) && (regEmail.value.length > 0) && (regPassword.value.length > 0) && (regConPassword.value === regPassword.value) && (regAgreement.checked === true)){
        subRegister.disabled = false;
        subRegister.classList.remove(...disableBtnForm);
        subRegister.classList.add(...enabledBtnForm);
    }else{
        subRegister.disabled = true;
        subRegister.classList.add(...disableBtnForm);
        subRegister.classList.remove(...enabledBtnForm);
    }
}

function validateEmail(email){
    const mailFormat = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (mailFormat.test(email)){
        return true;
    }
    
    return false;
}

function validateUsername(uname){
    const unameFormat = /^[\w.@+-]+$/;
    if (unameFormat.test(uname)){
        return true;
    }

    return false;
}


function showError(tb, errMessage){
    const inputContainer = (tb.parentElement).parentElement;
    const errorContainer = inputContainer.querySelector('.error');
    const errMsgContainer = inputContainer.querySelector('p');
    const errIcon = inputContainer.querySelector('#icError');
    const valIcon = inputContainer.querySelector('#icCheck');
    
    tb.classList.add('border-red-600');
    tb.classList.remove('border-med-turq');
    errorContainer.classList.remove('hidden'); // show the error
    errMsgContainer.innerText = errMessage; // replace error message
    errIcon.classList.remove('invisible'); // show error icon
    valIcon.classList.add('invisible'); // hide the check icon
}
function showValid(tb){
    const inputContainer = (tb.parentElement).parentElement;
    const errorContainer = inputContainer.querySelector('.error');
    const errIcon = inputContainer.querySelector('#icError');
    const valIcon = inputContainer.querySelector('#icCheck');
    
    tb.classList.remove('border-red-600');
    tb.classList.add('border-med-turq');
    errorContainer.classList.add('hidden'); // hide the error
    errIcon.classList.add('invisible'); // hide error icon
    valIcon.classList.remove('invisible'); // show the check icon
}


// when the page loads
window.onload = function(){
    subLogin.disabled = true; //disable the login button
    subRegister.disabled = true; // disable the register button
}