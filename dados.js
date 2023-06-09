function logar() {
    var loginUsuario = document.getElementById('nomedeusuario-login').value;
    var loginSenha = document.getElementById('password-login').value;

    if (loginUsuario == 'admin' && loginSenha == 'admin') {
        alert('Sucesso')
        location.href = "home.html"
    } else {
        alert('Usuario ou senha incorreta')
    }
}

function cadastro() {
    var cadUsuario = document.getElementById('nomedeusuario-cadastro').value;
    var cadEmail = document.getElementById('email-cadastro').value;
    var cadSenha = document.getElementById('password-cadastro').value;
    const termos = document.getElementById('termos');
    const botao = document.getElementById('btn-cad');
  
    botao.addEventListener('click', function() {
      if (!termos.checked) {
        alert('Por favor, aceite os termos e condições!');
      } else if (cadUsuario !== '' && cadEmail !== '' && cadSenha !== '') {
        alert('Cadastro efetuado!');
        location.href = "telaDeLogin.html";
      } else {
        alert('Usuário ou senha incorreta');
      }
    });
  }