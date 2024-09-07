tamanho = float(input("Entrada:\nDigite o tamanho do arquivo (em MB):"))
velocidade = float(input("Digite a velocidade do link de internet (em Mbps):"))

tempo = tamanho*8 /velocidade
minutos = tempo//60
segundos = tempo%60

print(f"\nEntrada:\nTempo aproximado para download: {minutos:.0f} minutos e {segundos:.0f} segundos.")