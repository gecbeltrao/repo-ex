def cadastrarcli():
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    listaclientes.append(nome)
    idadeclientes.append(idade)
    return(idade)

def cadastrarprod():
    produto = input("Digite o nome do produto: ")
    listaprodutos.append(produto)

maioridade = bool
listaclientes = []
idadeclientes = []
listaprodutos = []
listaprecos = []
while True:
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar produto")
    print("3 - Realizar venda")
    print("0 - Sair")
    op = int(input("Digite a opção escolhida: "))
    match op:
        case 1:
            idade = cadastrarcli()
            if idade >= 18:
                maioridade = True
            elif idade < 18:
                maioridade = False
        case 2:
            cadastrarprod()
            while True:
                preco = float(input("Digite o preço da unidade do produto: "))
                if preco <= 0:
                    print("O produto precisa ter um preço superior a 0, digite o preço novamente.")
                else:
                    listaprecos.append(preco)
                    break
        case 3:
            venda = input("Digite o nome do produto desejado: ")
            posicaoproduto = listaprodutos.index(venda)
            quantidade = int(input("Digite a quantidade de produtos a ser vendida: "))
            valorprod = float(listaprecos[posicaoproduto])
            valortotal = int(quantidade * valorprod)
            if valortotal >= 500:
                valortotal = valortotal * 0.9
            else:
                valortotal = valortotal
            print(f'O valor total da venda é de: R${valortotal:.2f}')
        case 0:
            print("Você saiu do programa.")
            break
        case _:
            print("Opção inválida.")