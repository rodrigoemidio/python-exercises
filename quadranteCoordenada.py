x = float(input("Entrada:\nCoordenada de um ponto P(x,y)\nDigite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x>0:
    if y>0:
        quadrante = "1°"
    else:
        quadrante = "4°"
else:
    if y>0:
        quadrante = "2°"
    else:
        quadrante = "3°"


print(f"\nSaída:\nO ponto P({x},{y}) pertence ao {quadrante} quadrante.")







