numero = int(input("Entrada:\nInsira um número inteiro: "))

if numero == 0:
    resultado = "nulo"
elif numero > 0:
    resultado = "positivo"
else:
    resultado = "negativo"


print(f"\nSaída:\nO número {numero} é {resultado}.")


