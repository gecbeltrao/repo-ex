def infocli():
    nome = input(f'Digite o nome do {i+1}º cliente: ')
    idade = input(f'Digite a idade do {i+1}º cliente: ')
    salario = input(f'Digite o salario do {i+1}º cliente: ')
    emp = input(f'Digite o valor do emprestimo do {i+1}º cliente: ')
    listanomes.append(nome)
    listaidades.append(idade)
    listasalarios.append(salario)
    listaemprestimos.append(emp)

listanomes = []
listaidades = []
listasalarios = []
listaemprestimos = []
qntcli = int(input("Digite a quantidade de clientes: "))

for i in range(qntcli):
    infocli()

for i in range(qntcli):
    risco = int()
    salario = int(listasalarios[i])
    idade = int(listaidades[i])
    emp = int(listaemprestimos[i])
    razao = float(emp / salario)
    if razao > 5:
        risco = 3
    elif razao > 3 and razao < 5:
        risco = 2
    else:
        risco = 1
    
    if idade < 25:
        risco = risco + 1
    
    if salario > 10000:
        risco = risco - 1
    
    print(f'O cliente é {listanomes[i]}.')
    print(f'Que tem um salário de R${salario:.2f}.')
    print(f'O valor do empréstimo solicitado é de R${emp:.2f}.')
    if risco >= 3:
        print("A operação é de alto risco.")
    elif risco == 2:
        print("A operação é de médio risco.")
    elif risco <= 1:
        print("A operação é de baixo risco.")