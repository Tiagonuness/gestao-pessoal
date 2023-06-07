const menubox = document.querySelector('.menubox')
const loginlink = document.querySelector('.login-link')
const registrarlink = document.querySelector('.registrar-link')

registrarlink.addEventListener('click', ()=> {
    menubox.classList.add('active');
})

loginlink.addEventListener('click', ()=> {
    menubox.classList.remove('active');
})

const inputsemail = document.querySelectorAll('.email-input[type="email"]');

inputsemail.forEach(input => {
  input.addEventListener('focus', function() {
    this.classList.add('placeholder-focused');
  });

  input.addEventListener('blur', function() {
    this.classList.remove('placeholder-focused');
  });
});

const inputspassword = document.querySelectorAll('.password-input[type="password"]');

inputspassword.forEach(input => {
  input.addEventListener('focus', function() {
    this.classList.add('placeholder-focused');
  });

  input.addEventListener('blur', function() {
    this.classList.remove('placeholder-focused');
  });
});

const inputusuario = document.querySelectorAll('.nomedeusuario[type="text"]');

inputusuario.forEach(input => {
  input.addEventListener('focus', function() {
    this.classList.add('placeholder-focused');
  });

  input.addEventListener('blur', function() {
    this.classList.remove('placeholder-focused');
  });
});