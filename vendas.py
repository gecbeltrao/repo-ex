def cadastrarprod():
    produto = input("Digite o nome do produto: ")
    listaprodutos.append(produto)

listaprodutos = []
listaprecos = []
listaquantidades = []
while True:
    print("1 - Cadastrar produto")
    print("2 - Vender produto")
    print("0 - Sair")
    op = int(input("Digite a opção escolhida: "))
    match op:
        case 1:
            cadastrarprod()
            while True:
                preco = float(input("Digite o preço da unidade do produto: "))
                if preco <= 0:
                    print("O produto precisa ter um preço superior a 0, digite o preço novamente.")
                else:
                    listaprecos.append(preco)
                    break
            while True:
                quantidadeprod = int(input("Digite a quantidade do produto no estoque: "))
                if quantidadeprod < 0:
                    print("O produto não pode ter uma quantidade negativa, digite a quantidade novamente.")
                else:
                    listaquantidades.append(quantidadeprod)
                    break
        case 2:
            while True:
                venda = input("Digite o nome do produto desejado: ")
                posicaoproduto = listaprodutos.index(venda)
                print(f'A quantidade do produto {listaprodutos[posicaoproduto]} é de {listaquantidades[posicaoproduto]}, ja seu preço é de R${listaprecos[posicaoproduto]:.2f}.')
                quantidadevenda = int(input("Digite a quantidade de produtos a ser vendida: "))
                listaquantidades[posicaoproduto] = int(listaquantidades[posicaoproduto]) - quantidadevenda
                valorprod = float(listaprecos[posicaoproduto])
                if int(listaquantidades[posicaoproduto]) < 0:
                    print("Não há esta quantidade de produtos no estoque, por favor digite um valor possível")
                    listaquantidades[posicaoproduto] = int(listaquantidades[posicaoproduto]) + quantidadevenda
                else:
                    valortotal = int(quantidadevenda * valorprod)
                    if valortotal >= 1000:
                        print("VENDA IMPORTANTE!!!")
                    print(f'O valor total da venda é de: R${valortotal:.2f}')
                    break
        case 0:
            print("Você saiu do programa.")
            break
        case _:
            print("Opção inválida.") 