frase = input("Digite uma frase: ").lower()
frase = frase.replace("rr", "l").replace("r", "l").replace("RR", "L").replace("R", "L")

print(f"Cebolinha diz: {frase}")


