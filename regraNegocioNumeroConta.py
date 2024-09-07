numero = input("Entrada\nDigite o número da conta com 4 algarismos: ")

soma = 0

for i in numero:
    soma += int(i)

digito = soma %10

print(f"\nSaída\nNúmero da conta completo: 00{numero}-{digito}")
