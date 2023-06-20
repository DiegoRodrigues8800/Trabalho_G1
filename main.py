lista_compras = []

def funcao_1():
    while True:
        item = input("Digite o item ou tecle Enter para voltar: ")
        if item == "":
            break
        quantidade = int(input("Qual a quantidade: "))
        preco = float(input("Qual o preço: "))
        produto = [item, quantidade, preco]
        lista_compras.append(produto)
        print("Item adicionado")

def funcao_2():
    for lista in lista_compras:
        print(lista)

def funcao_3():
    soma = sum(quantidade[1] for quantidade in lista_compras)
    print(f"Você tem {soma} produtos no seu carrinho.")

def funcao_4():
    if not lista_compras:
        print("Lista vazia. Adicione itens antes de procurar os itens mais baratos.")
    else:
        menor_preco = min(produto[2] for produto in lista_compras)
        itens_mais_baratos = [produto[0] for produto in lista_compras if produto[2] == menor_preco]
        print("Item mais barato:")
        for item in itens_mais_baratos:
            print(item)

def funcao_5():
    total = sum(produto[1] * produto[2] for produto in lista_compras)
    print(f"O valor total da compra é: R${total:.2f}")

def limpar_lista():
    lista_compras.clear()
    print("Lista de compras limpa com sucesso!")

while True:
    print("-=-=-=Lista de Compras Supermercado=-=-=-")
    print("1. Adicionar produtos.")
    print("2. Ver lista.")
    print("3. Total de produtos adicionados.")
    print("4. Item mais barato.")
    print("5. Valor total da compra.")
    print("6. Limpar a lista")
    print("0. Sair do sistema")
    print("-=-=-=Lista de Compras Supermercado=-=-=-"),
    try:
        escolha = int(input("Escolha uma opção: "))
    except Exception as ex:
        print("Deu erro")
    finally:
        print("Aba fechada.")

    if escolha == 1:
        try:
            funcao_1()
        except Exception as ex:
            print(f"Ocorreu um erro: {ex}")
        finally:
            print("Processo terminado")
    elif escolha == 2:
        try:
            funcao_2()
        except Exception as ex:
            print(f"Ocorreu um erro: {ex}")
        finally:
            print("Processo terminado")
    elif escolha == 3:
        try:
            funcao_3()
        except Exception as ex:
            print(f"Ocorreu um erro: {ex}")
        finally:
            print("Processo terminado")
    elif escolha == 4:
        try:
            funcao_4()
        except Exception as ex:
            print(f"Ocorreu um erro: {ex}")
        finally:
            print("Processo terminado")
    elif escolha == 5:
        try:
            funcao_5()
        except Exception as ex:
            print(f"Ocorreu um erro: {ex}")
        finally:
            print("Processo terminado")
    elif escolha == 6:
        try:
            limpar_lista()
        except Exception as ex:
            print(f"Ocorreu um erro: {ex}")
        finally:
            print("Processo terminado")
    elif escolha == 0:
        break
    else:
        print("Caracter Inválido")
