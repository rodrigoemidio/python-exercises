faturamento = float(input("Digite o faturamento da empresa: R$"))
custo = float(input("Digite o custo operacional: R$"))

lucro = faturamento - custo
lucro = f"R${lucro:_.2f}"


print(lucro.replace(".", ",").replace("_", "."))

