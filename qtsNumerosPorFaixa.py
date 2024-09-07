cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0

print("Entrada:")
while True:
    num = int(input("Digite um número positivo (-1 para sair): "))
    if num == -1: break
    while num<0:
        num = int(input("Esse número é negativo! Digite um número positivo: "))


    if num<=25:
        cont1 += 1
    elif num<=50:
        cont2 +=1
    elif num<=75:
        cont3 += 1
    elif num<=100:
        cont4 += 1


print(f"\nSaída\n[0-25]: {cont1} números")
print(f"[26-50]: {cont2} números")
print(f"[51-75]: {cont3} números")
print(f"[76-100]: {cont4} números")
