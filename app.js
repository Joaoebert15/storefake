function fetchProdutos() {
  fetch('store.json')
    .then(response => response.json()) 
    .then(data => {
      exibirProdutos(data); 
    })
    .catch(error => console.error('Erro ao buscar produtos:', error));
}


function exibirProdutos(produtos) {
  const container = document.getElementById('produtosContainer'); 
  container.innerHTML = '';

  produtos.forEach(produto => {
    const produtoDiv = document.createElement('div');
    produtoDiv.classList.add('produto');
    produtoDiv.innerHTML = `
      <h3>${produto.title}</h3>
      <p>Preço: $${produto.price}</p>
      <img src="${produto.image}" alt="${produto.title}" width="100" />
     
    `;
    container.appendChild(produtoDiv);
  });
}

window.onload = fetchProdutos;
