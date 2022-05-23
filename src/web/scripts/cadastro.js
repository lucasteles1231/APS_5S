async function cadastrar() {
  const empresa = document.getElementById("cadastro-empresa").value;
  const tipo = document.getElementById("cadastro-tipo").value;
  const quantidade = document.getElementById("cadastro-quantidade").value;
  const regiao = document.getElementById("cadastro-regiao").value;
  const descricao = document.getElementById("cadastro-descricao").value;

  console.log(empresa, tipo, quantidade, regiao, descricao);

  eel.RegisterEviction(empresa, tipo, quantidade, regiao, descricao)();
}