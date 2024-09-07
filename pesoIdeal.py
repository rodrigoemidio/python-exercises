altura = float(input("Entrada:\nDigite a altura da pessoa em metros: "))
sexo = input("Digite o sexo da pessoa m/f: ")

if sexo in "mM":
    peso =  (72.7*altura)-58
    print(f"\nSaída:\nO peso ideal dessa pessoa é {peso}Kg.")
elif sexo in "Ff":
    peso =  (62.1*altura)-44.7
    print(f"\nSaída:\nO peso ideal dessa pessoa é {peso}Kg.")
else:
    print("Sexo inválido. Tente novamente à meia noite.")






