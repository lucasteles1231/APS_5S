eel.expose(closeLoginScreen);
function closeLoginScreen() {
  window.close();
}

async function authenticate() {
  const user = document.getElementById("login-user").value;
  const password = document.getElementById("login-password").value;

  await eel
    .authenticate(user, password)()
    .then((result) => {
      if (result) {
        eel.openPage("login.html", "chat.html");
      } else {
        alert("Usuário e senha não coincidem!");
      }
    });
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