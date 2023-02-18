nome = input('Insira seu nome:')
nota1 = int(input(f'Olá {nome}! Insira sua primeira nota:'))
nota2= int(input('Agora, insira sua segunda nota:'))
media= (nota1+nota2)/2
print(f'{nome}, suas notas foram {nota1} e {nota2}.')
print(nome,', suas notas foram', nota1, 'e', nota2, '.')
print('%s, suas notas foram %s e %s, e sua média foi %s' %(nome, nota1, nota2, media))