votantes = 0
contador = 0
soma = 0

print("Entrada:")
for i in range(10):
    idade = int(input("Digite a idade do aluno: "))
    if idade >= 16:
        votantes += 1
    else:
        soma = soma + idade
        contador += 1

media = soma/contador

print(f"\nSaída:\nA quantidade de alunos que podem votar é {votantes}")
print(f"A media da idades dos alunos não eleitores é {media}")
