horaAula = float(input("Entrada\nDigite o valor da hora aula: R$"))
carga = float(input("Digite a carga horária semanal: "))

salario_base = horaAula * carga * 4.5
adicional = salario_base / 6
salario_final = salario_base + adicional

print(f"\nSaída\nSalário final: R${salario_final:.2f}")

