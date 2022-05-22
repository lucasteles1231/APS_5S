async function cadastrar() {
  const empresa = document.getElementById("cadastro-empresa").value;
  const tipo = document.getElementById("cadastro-tipo").value;
  const quantidade = document.getElementById("cadastro-quantidade").value;
  const regiao = document.getElementById("cadastro-regiao").value;
  const descricao = document.getElementById("cadastro-descricao").value;

  console.log(empresa, tipo, quantidade, regiao, descricao);

  eel
    .RegisterEviction(empresa, tipo, quantidade, regiao, descricao)()
    .then((result) => {
      if (result) {
        alert("Novo despejo cadastrado com sucesso!");
        document.getElementById("cadastro-empresa").value = "";
        document.getElementById("cadastro-tipo").value = "";
        document.getElementById("cadastro-quantidade").value = "";
        document.getElementById("cadastro-regiao").value = "";
        document.getElementById("cadastro-descricao").value = "";
      } else {
        alert(
          "Despejo não cadastrado, verifique se preencheu corretamente os campos!"
        );
      }
    });
}