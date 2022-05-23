eel.expose(closeChatScreen);

function closeChatScreen() {
  eel.stopWhile()();
  window.close();
}

// envia mensagem para o servidor
async function sendMessage() {
  var div = document.createElement("div");
  div.classList.add("balloon_right");
  var msg = document.getElementById("input_chat").value;
  document.getElementById("input_chat").value = "";
  var text = document.createTextNode(msg);
  div.appendChild(text);
  var element = document.getElementById("msg_div_main");
  element.appendChild(div);
  element.scrollTop = element.scrollHeight;
  sendMessageMain(msg, "chat")
}