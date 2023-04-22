'''
2- Faça uma programa em Python que peça do usuário um valor em graus para um
ângulo. Converta-o para radianos
 e, usando funções da biblioteca math, 
imprima o seno,
cosseno e tangente deste ângulo.

'''
import math

graus = float(input("Digite o valor em graus para um angulo: "))

radianos=math.radians(graus)

seno=math.sin(radianos)
cosseno=math.cos(radianos)
tangente=math.tan(radianos)

print("\n\nO radiano: %.2f"%radianos ,
    "\nO seno: %.2f "%seno,
    "\nO cosseno:%.2f "%cosseno,
    "\nA tangente: %.2f"%tangente)
