// Função utilizada para alterar a visualização das páginas
// Passa-se o id da div como parâmetro para que haja a comparação com a
// Lista de telas registradas, podendo assim definir qual tela será exibida ou não.

function changeScreen(screenName) {
  const screens = ["login", "dashboard", "chat", "cadastro"];
  
  for (let i = 0; i < screens.length; i++) {
    // Obtém o componente div a partir do id.
    var screen = document.getElementById(screens[i]);
    
    // Valida se o id informado na listagem de telas referencia um componente existente.
    if (screen === undefined || screen === null) continue;
    
    // Caso o id seja equivalente ao informado na chamada da função, a div será exibida
    // Senão, é aplicado o estilo "display: none" para que a visualização seja ocultada.
    if (screens[i] === screenName) {
      console.log('block');
      screen.style.display = "block";
      console.log(screen);
      console.log('block');
    } else {
      console.log('none');
      screen.style.display = "none";
    }
  }
}

// Função responsável por controlar a exibição do menu lateral
// e seus itens disponíveis no menu a partir do tipo de usuário.
function showMenu() {
  // Obtém o menu a partir do ID e da propriedade de classes do elemento.
  document.getElementById("controller-menu").style.display = "grid";
  
}

// Função executada ao iniciar a tela com o objetido de redimensionar
// A janela para o tamanho do monitor utilizado.
function onProgramStart() {
  window.moveTo(0, 0);
  window.resizeTo(screen.availWidth, screen.availHeight);
  eel.onStart();
}
onProgramStart();

// envia mensagem para o servidor
async function sendMessageMain(msg, screen) {
  eel.SendMessage(msg, screen)();
}

// recebe mensagem do servidor
function receiveMessage(msg, num, screen) {
  console.log(msg);
  console.log(screen);
  numMsg = parseInt(document.getElementById("num").value);
  if(numMsg<=num){

    // CHAT
    if (screen == "chat"){
      num += 1;
      document.getElementById("num").value = num.toString();
      var div = document.createElement("div");
      div.classList.add("balloon_left");
      var text = document.createTextNode(msg);
      div.appendChild(text);
      var element = document.getElementById("msg_div_main");
      element.appendChild(div);
      element.scrollTop = element.scrollHeight;
    
    // DASHBOARD
    } else if(screen == "dashboard"){
      
    // CADASTRO DE EMPRESA
    } else if(screen == "cadastro"){
      if (msg == "true") {
        alert("Novo despejo cadastrado com sucesso!");
        document.getElementById("cadastro-empresa").value = "";
        document.getElementById("cadastro-tipo").value = "";
        document.getElementById("cadastro-quantidade").value = "";
        document.getElementById("cadastro-regiao").value = "";
        document.getElementById("cadastro-descricao").value = "";
      } else {
        alert("Despejo não cadastrado, verifique se preencheu corretamente os campos!");
      }
    }

    // LOGIN
    else if(screen == "login"){
      msg = msg.split("  :  ");
      nome = msg[0];
      ico = msg[1];
      console.log(nome);
      console.log(ico);
      console.log(screen);
      if (nome == 'USER IS ALREADY CONNECTED') {
        alert("Usuário já conectado!");
      } else if (nome == 'USER DOES NOT EXIST') {
        alert("Usuário não existe!");
      } else {
        showMenu();
        document.getElementById("perfil__nome").textContent = nome;
        document.getElementById("perfil__icone").textContent = ico;
        changeScreen('chat');
      }
    }
  }
}
eel.expose(receiveMessage);