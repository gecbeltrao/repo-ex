def cadastrarcli():
    nome = input("Digite o nome do cliente: ")
    listacli.append(nome)

def cadastrarespec():
    while True:
        espec = input("Digite o nome da especialidade: ")
        if espec in listaespec:
            print("Esta especialidade já existe")
        else:
            listaespec.append(espec)
            break
        
def agendarconsulta():
    while True:
        nomecli = input("Digite o nome do cliente: ")
        if nomecli in listacli:
            listaconsultas.append(nomecli)
            while True:
                espec_consulta = input("Digite o nome da especialidade: ")
                if espec_consulta in listaespec:
                    listaconsultas.append(espec_consulta)
                    valorconsulta = input("Digite o valor da consulta: ")
                    listaconsultas.append(valorconsulta)
                    break
                else:
                    print("A especialidade não existe, tente novamente.")
            break
        else:
            print("Esse cliente não existe, tente novamente. ")

def realizarpagamento():
    while True:
        nomepagamento = input("Digite o nome do cliente que realizou a consulta: ")
        if nomepagamento in listaconsultas:
            poscli = int(listaconsultas.index(nomepagamento))
            print(poscli)
            break
        else:
            print("O cliente não existe ou não fez uma consulta, tente novamente.")
    valorfinal = listaconsultas[poscli+2]
    print(f'O valor a ser pago é de R${valorfinal}.')
    listaconsultas.pop(poscli)
    listaconsultas.pop(poscli)
    listaconsultas.pop(poscli)

def mostrarrelatorio():
    print(f'Os clientes são {listacli}')
    print(f'As especialidades são {listaespec}')
    print(f'As consultas pendentes estão listadas a seguir, sendo listadas em cliente, especialidade e valor {listaconsultas}')

listaespec = []
listacli = []
listaconsultas = []

while True:
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar especialidade")
    print("3 - Agendar consulta")
    print("4 - Realizar pagamento")
    print("5 - Mostrar relatório")
    print("0 - Sair")
    op = int(input("Digite a opção escolhida: "))
    match op:
        case 1:
            cadastrarcli()
        case 2:
            cadastrarespec()
        case 3:
            agendarconsulta()
        case 4:
            realizarpagamento()
        case 5:
            mostrarrelatorio()
        case 0:
            print("Você saiu do programa.")
            break
        case _:
            print("Opção inválida.")