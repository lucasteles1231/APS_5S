eel.expose(closeCadastroScreen);
function closeCadastroScreen() {
  window.close();
}

function irParaAnalytics() {
  eel.openPage("cadastro.html", "dashboard.html");
}

function irParaChat() {
  eel.openPage("cadastro.html", "chat.html");
}

async function cadastrar() {
  const name = document.getElementById("cadastro-name").value;
  const email = document.getElementById("cadastro-email").value;
  const password = document.getElementById("cadastro-password").value;
  const userType = document.getElementById("cadastro-type").value;

  eel
    .registerNewUser(name, email, password, userType)()
    .then((result) => {
      irParaAnalytics();
    });
}
