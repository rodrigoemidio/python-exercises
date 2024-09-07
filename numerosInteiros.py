contPos = 0
contNeg = 0
menor = 100000000000

while True:
    num = float(input("Digite um número (0 para sair):"))
    if  num == 0: break
    if num>0: contPos +=1
    else: contNeg += 1
    if num < menor:
        menor = num

print(f'{contPos} numeros positivos ')
print(f'{contNeg} numeros negativos')
print(f'o menor numero é {menor}')



