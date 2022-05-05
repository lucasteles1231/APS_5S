eel.expose(closeChatScreen);
function closeChatScreen() {
  window.close();
}

function teste() {
  const user = document.getElementById("login-user").value;
  eel.sendMessage()
}

function irParaAnalytics() {
  eel.openPage("chat.html", "dashboard.html");
}

function irParaUsuarios() {
  eel.openPage("chat.html", "cadastro.html");
}
