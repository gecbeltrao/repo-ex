def cadastrarfunc():
    nome = input("Digite o nome do funcionário: ")
    listanomes.append(nome)
    salario = float(input("Digite o salário do funcionário: "))
    listasalarios.append(salario)

listanomes = []
listasalarios = []

while True:
    print("1 - Cadastrar funcionário")
    print("2 - Checar dados")
    print("0 - Sair")
    op = int(input("Digite a opção escolhida: "))
    match op:
        case 1:
            cadastrarfunc()
        case 2:
            desconto = float()
            checar = input("Digite o nome do funcionário a ser checado: ")
            posicao = listanomes.index(checar)
            extra = float(input("Digite a quantidade de horas extras do funcionário: "))
            bonus = float(50 * extra)
            if float(listasalarios[posicao]) < 5000:
                salariofinal = float(listasalarios[posicao] * 1.05) + bonus
            elif float(listasalarios[posicao]) >= 5000 and float(listasalarios[posicao]) <= 10000:
                salariofinal = float(listasalarios[posicao]) + bonus
            elif float(listasalarios[posicao]) > 10000:
                desconto = float(listasalarios[posicao] * 0.1)
                salariofinal = float(listasalarios[posicao]) - desconto + bonus
            print(f'O salario base do funcionário {listanomes[posicao]} é de R${listasalarios[posicao]:.2f}, o bônus recebido foi de R${bonus:.2f}, seu salário final foi de R${salariofinal:.2f}.')
            if desconto > 0:
                print(f'O valor descontado do salário foi de R${desconto:.2f}')
        case 0:
            print("Você saiu do programa.")
            break
        case _:
            print("Opção inválida.")