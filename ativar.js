const menubox = document.querySelector('.menubox')
const loginlink = document.querySelector('.login-link')
const registrarlink = document.querySelector('.registrar-link')

registrarlink.addEventListener('click', ()=> {
    menubox.classList.add('active');
})

loginlink.addEventListener('click', ()=> {
    menubox.classList.remove('active');
})

// -------- EMAIL INPUT EXEMPLO -------- //
const emailInput = document.getElementById('email-input');

emailInput.addEventListener('focus', function() {
  emailInput.setAttribute('placeholder', 'exemplo@email.com');
});

emailInput.addEventListener('blur', function() {
  emailInput.removeAttribute('placeholder');
});

// -------- SENHA INPUT EXEMPLO -------- //
const passwordInput = document.getElementById('password-input');

passwordInput.addEventListener('focus', function() {
    passwordInput.setAttribute('placeholder', 'abcd1234');
});

passwordInput.addEventListener('blur', function() {
    passwordInput.removeAttribute('placeholder');
});

