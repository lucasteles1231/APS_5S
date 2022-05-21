/* function OpenChat() {
  document.getElementById("main_login").style.display = "none";
  document.getElementById("main_chat").style.display = "block";
  document.getElementById("main_dashboard").style.display = "none";
  document.getElementById("main_cadastro").style.display = "none";

  document.getElementById("sidebar_menu_item_chat").style.color = "#8d96b0";
  document.getElementById("sidebar_menu_item_chat").style.backgroundColor = "#f3e7ff";
  document.getElementById("sidebar_menu_item_chat").addEventListener("mouseover", function() {document.getElementById("sidebar_menu_item_chat").style.backgroundColor = "#f3e7ff";});
  document.getElementById("sidebar_menu_item_chat").addEventListener("mouseout", function() {document.getElementById("sidebar_menu_item_chat").style.backgroundColor = "#f3e7ff";});
  
  document.getElementById("sidebar_menu_item_dashboard").style.color = "#00000080";
  document.getElementById("sidebar_menu_item_dashboard").style.backgroundColor = "transparent";
  document.getElementById("sidebar_menu_item_dashboard").addEventListener("mouseover", function() {document.getElementById("sidebar_menu_item_dashboard").style.backgroundColor = "#f3e7ff30";});
  document.getElementById("sidebar_menu_item_dashboard").addEventListener("mouseout", function() {document.getElementById("sidebar_menu_item_dashboard").style.backgroundColor = "transparent";});

  document.getElementById("sidebar_menu_item_cadastro").style.color = "#00000080";
  document.getElementById("sidebar_menu_item_cadastro").style.backgroundColor = "transparent";
  document.getElementById("sidebar_menu_item_cadastro").addEventListener("mouseover", function() {document.getElementById("sidebar_menu_item_cadastro").style.backgroundColor = "#f3e7ff30";});
  document.getElementById("sidebar_menu_item_cadastro").addEventListener("mouseout", function() {document.getElementById("sidebar_menu_item_cadastro").style.backgroundColor = "transparent";});
} */

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