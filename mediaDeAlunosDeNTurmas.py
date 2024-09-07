import math

turmas = int(input("Entrada\nDigite a quantidade de turmas: "))
soma = 0

for i in range(turmas):
    alunos = int(input(f"Digite a quantidade de alunos da {i+1}ª turma: "))
    soma = soma + alunos


media = math.ceil(soma/turmas)

print(f"\nSaída\nAs turmas têm em média {media} alunos.")
