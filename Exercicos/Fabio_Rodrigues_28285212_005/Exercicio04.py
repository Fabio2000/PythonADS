agua = float(input("Digite o valor de conta de água que você paga: "))
luz = float(input("Digite o valor de conta de luz que você paga: "))
telefone = float(input("Digite o valor de conta de telefone que você paga: "))
salario = float(input("Digite seu salário: "))

total = agua+luz+telefone
resultado = salario - total
if salario >= total:
    print("Você consiguirá pagar todas as contas: ", resultado)
else:
    print("Salário insuficiente, trablhe mais.")