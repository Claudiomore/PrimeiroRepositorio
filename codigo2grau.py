import math

# Coeficientes da equação
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calcula o discriminante
discriminante = b**2 - 4*a*c

# Verifica se o discriminante é positivo, negativo ou zero
if discriminante > 0:
    # Duas raízes reais
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print("Duas raízes reais:")
    print("x1 =", x1)
    print("x2 =", x2)
elif discriminante == 0:
    # Uma raiz real (raiz dupla)
    x = -b / (2*a)
    print("Uma raiz real (raiz dupla):")
    print("x =", x)
else:
    # Nenhuma raiz real (raízes complexas)
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(-discriminante) / (2*a)
    print("Nenhuma raiz real (raízes complexas):")
    print("x1 =", realPart, "+", imaginaryPart, "i")
    print("x2 =", realPart, "-", imaginaryPart, "i")
