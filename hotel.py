def cadastrarhosp():
    nome = input("Digite o nome do hóspede: ")
    listahospedes.append(nome)

def cadastrarquarto():
    numeroquarto = int(input("Digite o número do quarto: "))
    listaquartos.append(numeroquarto)

listahospedes = []
listadocumentos = []
listaquartos = []
listatipos = []
while True:
    print("1 - Cadastrar hóspede")
    print("2 - Cadastrar quarto")
    print("3 - Fazer reserva")
    print("0 - Sair")
    op = int(input("Digite a opção escolhida: "))
    match op:
        case 1:
            cadastrarhosp()
            while True:
                documento = input("Digite o documento do hóspede: ")
                tamanho = int(len(documento))
                if tamanho >= 5:
                    listadocumentos.append(documento)
                    break
                else:
                    print("O documento do hóspede deve ter pelo menos 5 caracteres.")
        case 2:
            cadastrarquarto()
            while True:
                print("Qual o tipo do quarto?")
                print("1 - Quarto simples")
                print("2 - Quarto luxo")
                tipo = int(input("Digite o tipo escolhido: "))
                if tipo == 1 or tipo == 2:
                    listatipos.append(tipo)
                    break
                else:
                    print("Por favor selecione um dos tipos disponíveis.")
        case 3:
            nomeres = input("Digite o nome do hóspede: ")
            posicaohospede = listahospedes.index(nomeres)
            while True:
                print("Qual o tipo do quarto?")
                print("1 - Quarto simples")
                print("2 - Quarto luxo")
                tipoquarto = int(input("Digite o tipo do quarto a ser escolhido: "))
                if tipoquarto == 1:
                    precodia = int(150)
                    break
                elif tipoquarto == 2:
                    precodia = int(300)
                    break
                else:
                    print("Por favor selecione um dos tipos disponíveis.")
            dias = int(input("Digite a quantidade de dias de estadia: "))

            precototal = int(precodia * dias)
            if dias >= 7:
                precototal = precototal * 0.85
            else:
                precototal = precototal
            print(f'O valor final da hospedagem é de: R${precototal:.2f}')
        case 0:
            print("Você saiu do programa.")
            break
        case _:
            print("Opção inválida.") 