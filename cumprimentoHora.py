nome = input("Entrada:\nQual o seu nome? ")
horas = int(input("Que horas são [0-23]? "))

if horas>=5 and horas<=12:
    cumprimento = "Bom dia"
elif horas>=13 and horas<=18:
    cumprimento = "Boa tarde"
else:
    cumprimento = "Boa noite"

print(f"\nSaída:\n{cumprimento}, {nome}!")







