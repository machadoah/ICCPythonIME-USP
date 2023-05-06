import math

a = float(input("Insira de 'a', o coeficiente quadratico: "))
b = float(input("Insira de 'b', o coeficiente angular: "))
c = float(input("Insira de 'c', o coeficiente linear: "))

delta = ((b ** 2) - 4 * a * c)

if(delta > 0):
    
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    
    print("As raizes são {} e {}".format(x1, x2))
    
elif(delta == 0):
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    
    print("A raiz é {}".format(x1))
    
else:
    print("A equação não possui raizes reais!")
    
