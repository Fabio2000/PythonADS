compraValor = float(input("Digite o valor do seu produto para o devido desconto: "))

if compraValor >= 200:
    desconto = compraValor*20/100
    resultado = compraValor - desconto 
    print("Seu desconto será de 20% ", "R$",desconto, " valor totoal ", "R$",resultado)
else:
    print("Pelo valor do produto não temos nada por hoje, mas confira mais produtos de nossa loja e adquira o desconto de 20%")
