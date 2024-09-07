salario = float(input("Entrada:\nDigite o salário fixo: R$ "))
vendas = float(input("Digite o valor das vendas: R$ "))

comissao = vendas*0.04
salario = salario + comissao

print(f"\nSaída:\nComissão: R$ {comissao:.2f}\nSalário Final: R$ {salario:.2f}")


