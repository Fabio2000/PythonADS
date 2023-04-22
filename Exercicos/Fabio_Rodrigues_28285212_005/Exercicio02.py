#  Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a quantidade de
# horas trabalhadas, calcule e mostre o valor do salário. Considere os valores de horas a
# seguir, de acordo com o turno de trabalho. Caso o turno seja igual a ‘N’ (utilize um
# caractere para representar) o valor da hora trabalhada é R$ 45,00, caso contrário é R$
# 37,50

turnoT = str(input("Digite se voce faz turno, sim, ou não : "))
horasT = float(input("Digite suas horas trabalhadas: "))

if turnoT == 'Não' or turnoT == 'nao' or turnoT == 'n':
    resultado = 45 * horasT
    print("Seu calculo horas trabalhada de acordo sua resposta no turno, é: ", "R$",resultado)
else:
    resultado = 37.50 * horasT
    print("Seu calculo horas trabalhada de acordo sua resposta no turno, é: ", "R$",resultado)