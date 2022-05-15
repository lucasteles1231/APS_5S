eel.expose(closeChatScreen);
function closeChatScreen() {
  window.close();
}

// insere nome do usuario na tela de chat
function perfil() {
  eel
  .Name()()
  .then((result) => {
    document.getElementById("name").textContent = result[0];
    document.getElementById("ico").textContent = result[1];
  });
}
perfil();

// envia mensagem para o servidor
async function sendMessage() {
  var div = document.createElement("div");
  div.classList.add("balloon_right");
  var message = document.getElementById("input_chat").value;
  document.getElementById("input_chat").value = "";
  var text = document.createTextNode(message);
  div.appendChild(text);
  var element = document.getElementById("msg_div_main");
  element.appendChild(div);
  element.scrollTop = element.scrollHeight;
  var nome = "lucas";

  eel.SendMessage(message, nome)();
}

function receiveMessage(result) {
  console.log('waiting message!');
  if (result != false) {
    var message = result[0];
    var name = result[1];
    var div = document.createElement("div");
    div.classList.add("balloon_left");
    var text = document.createTextNode(message);
    div.appendChild(text);
    var element = document.getElementById("msg_div_main");
    element.appendChild(div);
    element.scrollTop = element.scrollHeight;
    initReceiveMessage();
  } else {
    initReceiveMessage();
  }
}
eel.expose(receiveMessage);


function irParaAnalytics() {
  eel.openPage("chat.html", "dashboard.html");
}

function irParaUsuarios() {
  eel.openPage("chat.html", "cadastro.html");
}
