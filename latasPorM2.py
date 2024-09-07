import math

tamanho = float(input("Entrada:\nDigite o tamanho da área a ser pintada em metros quadrados: "))
litros = tamanho/3
latas = litros/18
latas = math.ceil(latas)
valor = latas*80

print(f"\nSaída:\nVocê precisará comprar {latas} lata(s).\nO valor total a pagar será de R${valor}.")







