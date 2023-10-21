lista_pecas = []  # lista que armazena os dicionarios de cada peça


# --------------------inicio de cadastrarPeca-----------------------
def cadastrarPeca(codigo):  # função que cadastra peças
    print("Bem vindo ao MENU de cadastro de peça")
    print("O código da peça é : {:0>3}".format(codigo))
    nome = input("Insira o nome da peça:")
    fabricante = input("Insira o fabricante da peça:")
    valor = float(input("Insira o valor(R$) da peça :"))
    dicionario_pecas = {
        "codigo": codigo,  # lista do dicionarios
        "nome": nome,
        "fabricante": fabricante,
        "valor": valor,
    }
    lista_pecas.append(dicionario_pecas.copy())  # copia para o dicionario


# ---------------------Fim de cadastrarPeca------------------------


# ---------------------inicio de consultarPeca----------------------
def consultarPeca():
    while True:  # validação da resposta
        try:
            print(
                "Bem vindo ao MENU de consulta de peças"
            )  # opçoes de consulta para o cliente
            consultar = input(
                "\nDigite a opção desejada :\n"
                + "1-consultar todas as peças\n"
                + "2-consultar peças por código\n"
                + "3-consultar peça por fabricante\n"
                + "4-retornar"
                + "\n>>"
            )

            if consultar == "1":
                print("Você escolheu consultar todas as peças")
                for peca in lista_pecas:  # seleciona cada dicionario na lista
                    print("------------------------------")
                    for (
                        key,
                        value,
                    ) in (
                        peca.items()
                    ):  # varre todos os conjunto chave e valor do dicionario
                        print("{} : {}".format(key, value))
                    print("-------------------------")
            elif consultar == "2":
                print("Você escolheu consultar peças por código")
                entrada = int(input("Insira o código desejado:"))
                for peca in lista_pecas:  #
                    if peca["codigo"] == entrada:
                        print("-------------------------")
                        for key, value in peca.items():  #
                            print("{} : {}".format(key, value))
                    print("--------------------------")
            elif consultar == "3":
                print("Você escolheu consultar peça por fabricante")
                entrada = input("Digite o fabricante desejado:")
                for peca in lista_pecas:  #
                    if peca["fabricante"] == entrada:
                        print("---------------------------")
                        for key, value in peca.items():  #
                            print("{} : {}".format(key, value))
                        print("----------------------------")
            elif consultar == "4":
                return  # Sai da função consultarpeca e volta para ao menu
            else:
                print(
                    "Pare de digitar números que não exitem..."
                )  # exibe caso números fora do menu sejam digitados
                continue
        except ValueError:
            print(
                "Erro.Você digitou um valor não inteiro!"
            )  # mensagem exibida caso um número não inteiro é digitado


# -------------------Fim  de consultarPeca------------------


# -------------------inicio de removerPeca-----------------
def removerPeca():  # função para remover peça do estoque
    print("Bem vindo ao MENU de remover peças")
    entrada = int(input("Digite o código da peça que deseja remover:"))
    for peca in lista_pecas:
        if peca["codigo"] == entrada:
            lista_pecas.remove(peca)
            print(
                "Peça removida com sucesso!"
            )  # exibe mensagem sinalizando a remoção da peça


# -----------------------Fim do removerPeca-------------------

# ----------------------------inicio Main------------------------

print("Bem vindo ao controle de estoque da bicicletaria Go go")

registro_ru = 0  # (contador de registro de peças)
while True:
    try:
        opcoes = int(
            input(
                "Digite a opção desejada:\n"
                + "1-Cadastrar peças\n"
                + "2-Consultar peças\n"
                + "3- Remover peças\n"
                + "4- Sair\n"
                + ">>"
            )
        )
        if opcoes == 1:
            registro_ru = registro_ru + 1
            cadastrarPeca(registro_ru)
        elif opcoes == 2:
            consultarPeca()
        elif opcoes == 3:
            removerPeca()
        elif opcoes == 4:
            print("Programa encerrado")
            break
        else:
            print("Opção inválida.Digite novamente!")
            continue
    except ValueError:
        print("Pare de digitar números que não existe...")
# -------------------Fim Main----------------------
