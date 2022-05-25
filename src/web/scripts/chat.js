eel.expose(closeChatScreen);

function closeChatScreen() {
  eel.stopWhile()();
  window.close();
}

function enviarEnter(e){
    var tecla=(window.event)?event.keyCode:e.which;
    if (tecla == 13)
    {
      sendMessage();
    }
}

// envia mensagem para o servidor
async function sendMessage() {
  var msg = document.getElementById("input_chat").value;
  if (!msg == "") {
    var div = document.createElement("div");
    div.classList.add("balloon_right");
    document.getElementById("input_chat").value = "";
    var text = document.createTextNode(msg);
    div.appendChild(text);
    var element = document.getElementById("msg_div_main");
    element.appendChild(div);
    element.scrollTop = element.scrollHeight;
    sendMessageMain(msg, "chat")
  }
}