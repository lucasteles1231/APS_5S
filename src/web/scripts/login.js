function authenticate() {
  var user = document.getElementById("login_user").value;
  console.log(user);
  var password = document.getElementById("login_password").value;
  console.log(password);
  if(user != "" && password != "") {
    var msg = user + "  :  " + password.toString();
    sendMessageMain(msg, "login");
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
      eel.initThread()();
    } else {
      alert("Conexão deu errado!!");
    }
  });
}