eel.expose(closeLoginScreen);
function closeLoginScreen() {
  window.close();
}

function authenticate() {
  const user = document.getElementById("login-user").value;
  const password = document.getElementById("login-password").value;
  if(user != "" && password != "") {
      eel.authenticate(user, password)()
      .then((result) => {
        if (result == 'CONFIRMED USER') {
          eel.openPage("login.html", "chat.html");
        } else if (result == 'USER IS ALREADY CONNECTED') {
          alert("Usuário já conectado!");
        } else if (result == 'USER DOES NOT EXIST') {
          alert("Usuário não existe!");
        }
      });
  } else {
    alert("Por favor insira usuario e senha!");
  }
}

function connect() {
  const ipPort = document.getElementById("ip-connection").value;
  eel.startConnection(ipPort)()
  .then((result) => {
    if (result) {
      document.getElementById('login-user').disabled = false;
      document.getElementById('login-password').disabled = false;
      alert("Conexão concluída!!");
    } else {
      alert("Conexão deu errado!!");
    }
  });
}