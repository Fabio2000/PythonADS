a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a == 0:
    print("Não é equação do segundo grau")
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + (delta**0.5))/(2*a)
        x2 = (-b - (delta**0.5))/(2*a)
        print("As raízes da equação são:", x1, "e", x2)
    elif delta == 0:
        x = -b/(2*a)
        print("A raiz da equação é:", x)
    else:
        print("Não há raízes reais")