nome = input('Insira seu nome:')
disciplina = input(f'Olá {nome}! Qual sua disciplina?')
nota1 = float(input('Insira sua primeira nota:'))
nota2= float(input('Agora, insira sua segunda nota:'))
media= (nota1+nota2)/2
print('Nome do aluno: %s\n Disciplina: %s\n Primeira nota: %.2f \n Segunda nota: %.2f\n Média: %s' %(nome, disciplina, nota1, nota2, media))
