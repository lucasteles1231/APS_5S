eel.expose(closeChatScreen);

var intervalID;

function closeChatScreen() {
  eel.stopWhile()();
  stopInterval;
  window.close();
}

function contatos(){
  console.log('entrou');
  eel
  .Contacts()()
  .then((result) => {
    console.log(result);
    if(result.length != 0){
      var divDel = document.getElementById("contacts");
        
      while(divDel.firstChild) {
        divDel.removeChild(divDel.firstChild);
      };

      console.log('entrou no if');
      function addContactsInHTML(item, indice){
        console.log('entrou na função');
        var div = document.createElement("div");
        div.classList.add("contact");
        div.setAttribute("id", "contact " + indice.toString());
        var text = document.createTextNode(item);
        div.appendChild(text);
        var element = document.getElementById("contacts");
        element.appendChild(div);
        var div = document.getElementsByClassName("contact");
        document.getElementById("contact " + indice.toString()).onclick = function() {
          document.getElementById("contacts").style.display = "none";
          document.getElementById("chat__mensagens").style.display = "block";
          document.getElementById("contact_name_chat").innerHTML = item;
          stopInterval();
        };
      };
      result.forEach(addContactsInHTML);
    }
  });
}

function stopInterval(){
  clearInterval(intervalID);
  eel.initThread()();
}

function timer() {
  intervalID = setInterval(() => {
    contatos()
  }, 1000);
}


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
  var nome = document.getElementById("contact_name_chat").innerHTML;
  console.log(nome);
  eel.SendMessage(message, nome)();
}

function receiveMessage(result, num) {
  numMsg = document.getElementById("num").value;
  numMsg = parseInt(numMsg);
  console.log('waiting message!');
  console.log(num)
  console.log(result)
  console.log(numMsg)
  console.log(numMsg <= num)
  if(numMsg<=num){
    num += 1;
    document.getElementById("num").value = num.toString();
    var message = result[0];
    var name = result[1];
    var div = document.createElement("div");
    div.classList.add("balloon_left");
    var text = document.createTextNode(message);
    div.appendChild(text);
    var element = document.getElementById("msg_div_main");
    element.appendChild(div);
    element.scrollTop = element.scrollHeight;
  }
}

eel.expose(receiveMessage);