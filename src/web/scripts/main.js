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



// insere nome do usuario na tela de chat
function perfil() {
  eel
  .Name()()
  .then((result) => {
    document.getElementById("perfil__nome").textContent = result[0];
    document.getElementById("perfil__icone").textContent = result[1];
  });
}

// Função executada ao iniciar a tela com o objetido de redimensionar
// A janela para o tamanho do monitor utilizado.
function onProgramStart() {
  window.moveTo(0, 0);
  window.resizeTo(screen.availWidth, screen.availHeight);
  eel.onStart();
}

onProgramStart();

eel.HowLastScreen()()
.then((result) => {
  if (result != '') {
    showMenu();
    perfil();
    timer();
    changeScreen(result);
  }
});