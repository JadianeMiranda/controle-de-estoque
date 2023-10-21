# controle-de-estoque🚲
Um programa simples feito com Python, que faz o controle de estoque de peças de uma loja de bicicletaria. Possibilita o cadastro, consulta e remoção de peças do inventário da loja.

#  Como funciona⚙️ :

É muito simples:

1-  O programa começa com a definição de uma lista vazia chamada lista_pecas, que será usada para armazenar os dicionários de informações de cada peça.

2-  Em seguida, há uma função chamada cadastrarPeca(codigo) que permite ao usuário cadastrar uma nova peça. Ela solicita informações como nome, fabricante e valor da peça, cria um dicionário com essas informações e, em seguida, adiciona esse dicionário à lista lista_pecas.

3-  A função consultarPeca() permite ao usuário consultar as peças do estoque. Ele oferece várias opções, como listar todas as peças, procurar por código ou fabricante. Dependendo da escolha do usuário, ele itera sobre os dicionários na lista lista_pecas e exibe as informações correspondentes.

4-  A função removerPeca() permite ao usuário remover uma peça do estoque com base no código fornecido. Ele pesquisa a lista lista_pecas em busca do código correspondente e remove a peça, se encontrada.

5-  O programa principal começa com um loop infinito onde o usuário pode escolher entre diferentes opções, como cadastrar peças, consultar peças, remover peças ou sair do programa. Cada opção chama a função correspondente.

6-  O programa lida com exceções, como quando o usuário digita um valor que não é um número inteiro.


