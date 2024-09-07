num1 = float(input("Entrada:\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("[1] Média")
print("[2] Diferença maior-menor")
print("[3] Produto")
print("[4] Divisão n1/n2")
opcao = input("Digite uma opção: ")

if opcao not in "1234":
    print ("Opção inválida!")
else:
    if opcao=="1":
        media = (num1+num2)/2
        print(f'Média = {media:.2f}')
    elif opcao=="2":
        if num1>num2:
            dif = num1-num2
            print(f'Diferença = {dif}')
        elif num1<num2:
            dif = num2-num1
            print(f'Diferença = {dif}')
        else:
            print(f'Diferença = 0')
    elif opcao=="3":
        prod = num1*num2
        print(f'Produto = {prod}')
    else:
        if num2 == 0:
            print("Impossível dividir por zero!!!!!")
        else:
            div = num1/num2
            print(f'Divisão = {div}')










