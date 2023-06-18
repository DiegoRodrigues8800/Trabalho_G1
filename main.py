lista_compras = []
def funcao_1 ():
    while True:
        item = input("Digite o item ou tecle Enter para voltar: ")
        if item == "":
            break
        quantidade = int(input("Qual a quantidade: "))
        preco = float(input("Qual o preço: "))
        produto = [item,quantidade,preco]
        lista_compras.append(produto)
        print("Item adicionado")
def funcao_2():
    for lista in lista_compras:
        print(lista)
def funcao_3():
    soma = 0
    for quantidade in lista_compras:
        soma = soma + quantidade[1]
    print(f"Você tem {soma} produtos no seu carrinho.")
while True:
    print("-=-=-=Lista de Compras Supermercado=-=-=-")
    print("1. Primeira Função")
    print("2. Segunda Função")
    print("3. Terceira Função")
    print("4. Quarta Função")
    print("5. Quinta Função")
    print("6. Sexta Função")
    print("7. Sétima Função")
    print("8. Oitava Função")
    print("9. Nona Função")
    print("0. Sair do sistema")
    print("-=-=-=Lista de Compras Supermercado=-=-=-")
    escolha = int(input("Escolha uma opção: "))
    match escolha:
        case 1:
            try:
                funcao_1()
            except Exception as ex:
                print(f"Deu Erro qualquer: {ex}")
            finally:
                print("Processo terminado")
        case 2:
            try:
                funcao_2()
            except Exception as ex:
                print(f"Deu Erro qualquer: {ex}")
            finally:
                print("Processo terminado")
        case 3:
            try:
                funcao_3()
            except Exception as ex:
                print(f"Deu Erro qualquer: {ex}")
            finally:
                print("Processo terminado")
        case 4:
            print("Quarta Função")
        case 5:
            print("Quinta Função")
        case 6:
            print("Sexta Função")
        case 7:
            print("Sétima Função")
        case 8:
            print("Oitava Função")
        case 9:
            print("Nona Função")
        case 0:
            break
        case _:
            print("Carácter Inválida")
