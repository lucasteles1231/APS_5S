// Função utilizada para alterar a visualização das páginas
// Passa-se o id da div como parâmetro para que haja a comparação com a
// Lista de telas registradas, podendo assim definir qual tela será exibida ou não.

function verificaUser() { 
  var tipoUser = 1; //Alterar aqui para tipo usuario
  if (tipoUser != 1) {
    document.getElementById("usuarios-btn").style.display = "none";
  }
}

function changeScreen(screenName) {
  const screens = ["login", "dashboard", "chat", "cadastro"];
  
  for (let i = 0; i < screens.length; i++) {
    // Obtém o componente div a partir do id.
    var screen = document.getElementById(screens[i]);
    
    // Valida se o id informado na listagem de telas referencia um componente existente.
    if (screen === undefined || screen === null) continue;
    
    // Caso o id seja equivalente ao informado na chamada da função, a div será exibida
    // Senão, é aplicado o estilo "display: none" para que a visualização seja ocultada.
    switch (screenName) {
      case "chat":
        document.getElementById("chat-btn").classList.add("selected");
        document.getElementById("usuarios-btn").classList.remove("selected");
        document.getElementById("dashboard-btn").classList.remove("selected");

        document.getElementById("header-titulo").innerHTML = "CHAT";
        break;
      case "cadastro":
        document.getElementById("chat-btn").classList.remove("selected");
        document.getElementById("usuarios-btn").classList.add("selected");
        document.getElementById("dashboard-btn").classList.remove("selected");

        document.getElementById("header-titulo").innerHTML = "CADASTRO DE DESPEJOS";
        break;
      case "dashboard":
        document.getElementById("chat-btn").classList.remove("selected");
        document.getElementById("usuarios-btn").classList.remove("selected");
        document.getElementById("dashboard-btn").classList.add("selected");

        document.getElementById("header-titulo").innerHTML = "DASHBOARD";
        break;
    }
    if (screens[i] === screenName) {
      console.log('block');
      screen.style.display = "block";
      eel.SaveScreen(screenName);
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
eel
.onStart()()
.then((result) => {
  if(result[0] != "" && result[0] != "login"){
    refresh(result);
  } else if(result[2].length != 0 && result[3].length !=0){
    document.getElementById('form_login').style.display = "block";
    document.getElementById('form_ip_con').style.display = "none";
    document.getElementById('login_user').disabled = false;
    document.getElementById('login_password').disabled = false;
  }
});

function refresh(dados){
  showMenu();
  if (dados[4] == "Usuario"){
    document.getElementById("usuarios-btn").style.display = "none";
    document.getElementById("dashboard-btn").style.display = "none";
  }
  document.getElementById("perfil__nome").textContent = dados[1];
  document.getElementById("perfil__icone").textContent = dados[1].split("")[0].toUpperCase();
  console.log(dados[0]);
  changeScreen(dados[0]);
  timer();
}

function timer() {
  setInterval(() => {
    sendMessageMain("", "dashboard")
  }, 3000);
}

// envia mensagem para o servidor
async function sendMessageMain(msg, screen) {
  eel.SendMessage(msg, screen)();
}

// recebe mensagem do servidor
function receiveMessage(msg, screen) {
  console.log(msg);
  console.log(screen);

  if (typeof msg === "string"){

    // CHAT
    if (screen == "chat"){
      var splitmsg =  msg.split("  :  ");
      var div = document.createElement("div");
      div.classList.add("balloon_left");

      var h6 = document.createElement("h6");
      h6.style.color = "red";
      
      var nome = document.createTextNode(splitmsg[1]);
      h6.appendChild(nome);
      div.appendChild(h6);
      
      var text = document.createTextNode(splitmsg[0]);
      div.appendChild(text);

      
      var element = document.getElementById("msg_div_main");
      element.appendChild(div);
      element.scrollTop = element.scrollHeight;
    }
      // CADASTRO DE EMPRESA
    else if(screen == "cadastro"){
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
      nivel = msg[2];
      console.log(nome);
      console.log(ico);
      console.log(screen);
      if (nome == 'USER IS ALREADY CONNECTED') {
        alert("Usuário já conectado!");
      } else if (nome == 'USER DOES NOT EXIST') {
        alert("Usuário não existe!");
      } else {
        showMenu();
        if (nivel == "Usuario"){
          document.getElementById("usuarios-btn").style.display = "none";
          document.getElementById("dashboard-btn").style.display = "none";
        }
        document.getElementById("perfil__nome").textContent = nome;
        document.getElementById("perfil__icone").textContent = ico;
        changeScreen('chat');
        timer();
      }
    }
  } else{
    // DASHBOARD
     if(screen == "dashboard"){
  
      var tbl = document.getElementById("table_dashboard").rows.length;
      tbl = tbl - 1;
      for (let i=1; i<=tbl; i++)  {
        document.getElementById("table_dashboard").deleteRow(1);
      };
      var dpjLitro = 0;
      var dpjQuilo = 0;
      var tamRows = msg.length;
      console.log(tamRows != 0);
      if(tamRows != 0){
        for (let j=0; j<tamRows; j++){
          var thisrow = msg[j];
          const splitrow = thisrow.split("  :  ");
          if(splitrow[2] == "Litro"){
            console.log(dpjLitro);
            console.log(parseFloat(splitrow[3]));
            dpjLitro += parseFloat(splitrow[3]);
            console.log(dpjLitro);
          } else if(splitrow[2] == "Mililitro"){
            console.log(dpjLitro);
            console.log(parseFloat(splitrow[3]) / 1000);
            dpjLitro += parseFloat(splitrow[3]) / 1000;
            console.log(dpjLitro);
          } else if(splitrow[2] == "Quilograma") {
            console.log(dpjQuilo);
            console.log(parseFloat(splitrow[3]));
            dpjQuilo += parseFloat(splitrow[3]);
            console.log(dpjQuilo);
          } else if(splitrow[2] == "Tonelada"){
            console.log(dpjQuilo);
            console.log(parseFloat(splitrow[3]) * 1000);
            dpjQuilo += parseFloat(splitrow[3]) * 1000;
            console.log(dpjQuilo);
          }
          var tr = document.createElement("tr");
          var td1 = document.createElement("td");
          var id = document.createTextNode(splitrow[0]);
          td1.appendChild(id);
          tr.appendChild(td1);
          var td2 = document.createElement("td");
          var company = document.createTextNode(splitrow[1]);
          td2.appendChild(company);
          tr.appendChild(td2);
          var td5 = document.createElement("td");
          var region = document.createTextNode(splitrow[4]);
          td5.appendChild(region);
          tr.appendChild(td5);
          var td6 = document.createElement("td");
          var description = document.createTextNode(splitrow[5]);
          td6.appendChild(description);
          tr.appendChild(td6);
          var td3 = document.createElement("td");
          var typeEviction = document.createTextNode(splitrow[2]);
          td3.appendChild(typeEviction);
          tr.appendChild(td3);
          var td4 = document.createElement("td");
          var qty = document.createTextNode(splitrow[3]);
          td4.appendChild(qty);
          tr.appendChild(td4);
          var tbody = document.getElementById("tbody_dashboard");
          tbody.appendChild(tr);
          document.getElementById("num_casos_dash").innerHTML = tamRows;
          document.getElementById("num_despejo_peso").innerHTML = dpjQuilo;
          document.getElementById("num_despejo_litro").innerHTML = dpjLitro;
        }
      }
    }
  }
}
eel.expose(receiveMessage);