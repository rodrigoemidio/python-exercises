nota1 = float(input("Entrada:\nDigite a primeira nota parcial:"))
nota2 = float(input("Digite a segunda nota parcial:"))
media = (nota1+nota2)/2

if media>=9:
    conceito = "A"
elif media>=7.5:
    conceito = "B"
elif media>=6:
    conceito = "C"
elif media>=4:
    conceito = "D"
else:
    conceito = "E"

mensagem = "APROVADO" if conceito in "ABC" else "REPROVADO"

print(f"\nSaída:\nConceito: {conceito}\nMensagem: {mensagem}.")







