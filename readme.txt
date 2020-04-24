Trabalho de Desenvolvimento Web
Patrícia Martins Rocca Crestani

TEMA: Venda de gatos e de produtos para o seu animal de estimação.

RESUMO: O site "The Cat Store" vem com o intuito de promover a adoção de animais, assim como a doação
para ONGs que resgatam animais de rua. Realizando uma falsa venda de gatos, que na realidade estão
disponíveis para adoção nas mesmas ONGs citadas.

TRABALHO 1: O site atualmente possui 4 páginas HTML:
    index.html que é a home;
    produto.html que é aonde vemos a descrição do produto "Cookie";
    quemsomos.html que descreve o objetivo do site; e
    carrinho.html que apresenta um carrinho fictício que será implementado futuramente.

Além das funcionalidades vistas em sala, este site possui também:
    Carousel na página index.html, mostrando as imagens dos produtos;
    Tabela para descrição do gato em produto.html;
    Alert ao clicar em Adicionar ao Carrinho em produto.html;
    Badge na página index.html no produto "Cookie"; e
    Toast na página carrinho.html ao clicar em "Finalizar Compra".

TRABALHO 2: O form adicionado ao site se encontra em quemsomos.html na parte de Fale Conosco, com: um campo texto
indicando o e-mail de quem manda a mensagem; uma caixa dropdown para indicar o assunto da mensagem a ser enviada;
uma caixa de texto grande (textarea) para a mensagem; botões de radio para sinalizar se o usuário quer receber
novidades por e-mail; checkboxes para indicar sobre qual assunto o usuário quer receber e-mails.

Todos os campos possuem validação, encontrada no arquivo script.js. Para confirmar que as informações foram
enviadas com sucesso, uma Toast aparece no canto superior direito da tela.

TRABALHO 3: Os botões de like/dislike foram adicionados a página "produto.html".

TRABALHO 4: As imagens e textos dos produtos e gatos foram feitas através de consultas ao banco de dados.
Também foi implementado o campo Slug para os itens. No estado atual o site encontra-se com apenas itens de exemplo.
Mais itens serão cadastrados para o próximo trabalho, visto que serão inclusos formulários para cadastro dos mesmos.

TRABALHO 5: A pesquisa por produtos funciona. É possível criar, editar e remover produtos pela aba
de administração (engrenagem no topo direito da página). Também há paginação em todas as páginas.

TRABALHO 6: O login/logout foi implementado no site. Usuários criados pelo comando createsuperuser podem realizar
login no site normalmente. O carrinho (com sua adição, remoção e atualização) também funciona, contanto que
o usuário esteja logado.