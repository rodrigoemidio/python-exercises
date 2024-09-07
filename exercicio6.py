#declaração das listas
salarios = []
nomes = []
gratificacoes = []

#solicitação dos dados ao usuário
while True:
    nome = input("Digite o nome do funcionário: ").title()
    if nome == "": break 
    nomes.append(nome)
    salario = float(input(f"Digite o salário de {nome}: R$"))
    salario = salario*1.03
    salarios.append(salario)
    
    if salario <1000: gratificacoes.append(200)
    elif salario <1500: gratificacoes.append(150)
    elif salario <2500: gratificacoes.append(100)
    else: gratificacoes.append(50)
        

#solicitar ao usuário o nome do funcionário

n = input("Digite o nome do usuário que você deseja consultar: ")
n = n.title()
if n not in nomes: print(f"O funcionário {n} não consta na lista.")
else:
    i = nomes.index(n)
    print(f"O funcionário {nomes[i]} recebe: R${salarios[i] + gratificacoes[i]}")
    




#print(nomes)
#n = input("Digite um nome par excluir: ")
#if n in nomes:
#    i = nomes.index(n)
#    nomes.pop(i)
#else: print(f"O nome {n} não foi encontrado. ")
#print(nomes)