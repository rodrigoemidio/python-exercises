contador = 0

print("Entrada: ")
while True:
    resp = input("Já dormiu? (s/n)")
    if resp in "nN":
        contador +=1
    elif resp in "sS":
        break

print (f"\nSaída:\nVocê contou {contador} carneirinhos.")