function authenticate() {
  const user = document.getElementById("login_user").value;
  const password = document.getElementById("login_password").value;
  if(user != "" && password != "") {
      eel.Authenticate(user, password)()
      .then((result) => {
        if (result == 'USER IS ALREADY CONNECTED') {
          alert("Usuário já conectado!");
        } else if (result == 'USER DOES NOT EXIST') {
          alert("Usuário não existe!");
        } else {
          showMenu();
          perfil();
          timer();
          changeScreen('chat');
          eel.SaveLastScreen('chat')();
        }
      });
  } else {
    alert("Por favor insira usuario e senha!");
  }
}

function startConnection() {
  var Ip = document.getElementById("ip_connection").value;
  var Port = document.getElementById("port_connection").value;
  const ipPort = Ip + ":" + Port;
  eel.StartConnection(ipPort)()
  .then((result) => {
    if (result) {
      document.getElementById('form_login').style.display = "block";
      document.getElementById('form_ip_con').style.display = "none";
      document.getElementById('login_user').disabled = false;
      document.getElementById('login_password').disabled = false;
    } else {
      alert("Conexão deu errado!!");
    }
  });
}