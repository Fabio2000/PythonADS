'''
1- Escreva um programa em Python para calcular o valor de uma prestação em atraso
(prestacao). Para isso, obtenha o valor da prestação (valorPrestacao), a porcentagem de
multa pelo atraso (multa) e a quantidade de dias de atraso (qtdeDias). Calcular e mostrar o
valor da prestação atualizado, sabendo que:
prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)


2- Faça uma programa em Python que peça do usuário um valor em graus para um
ângulo. Converta-o para radianos e, usando funções da biblioteca math, imprima o seno,
cosseno e tangente deste ângulo.

'''
valorPrestacao = float(input("Digite o valor da prestação: "))
multa = float(input("Digite o valor da porcentagem: "))
qtdeDias = int(input("Digite a quantidade de dias: "))


prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)
print(prestacao)
