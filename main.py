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
            print("Primeira Função")
        case 2:
            print("Segunda Função")
        case 3:
            print("Terceira Função")
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
