segundo = float(input("Entrada:\nDigite uma quantidade de segundos:"))

hora = (segundo/60)//60
minuto = (segundo//60)-hora*60
segundo = (segundo%60)


print(f"\nSaída:\n{hora:.0f} hora(s), {minuto:.0f} minuto(s) e {segundo:.0f} segundo(s) ")


