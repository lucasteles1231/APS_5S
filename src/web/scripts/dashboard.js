eel.expose(closeDashboardScreen);
function closeDashboardScreen() {
  window.close();
}


function irParaChat() {
  eel.openPage("dashboard.html", "chat.html");
}

function irParaUsuarios() {
  eel.openPage("dashboard.html", "cadastro.html");
}