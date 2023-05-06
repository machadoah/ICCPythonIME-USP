import math

print("Insira as coordenadas de um ponto 'p'!")

Xp = float(input("Insira o valor de 'x' na coordenada: "))
Yp = float(input("Insira o valor de 'y' na coordenada: "))

print("Insira as coordenadas de um ponto 'q'!")

Xq = float(input("Insira o valor de 'x' na coordenada: "))
Yq = float(input("Insira o valor de 'y' na coordenada: "))

distancia = math.sqrt(((Xp - Xq) ** 2) + ((Yp - Yq) ** 2))

# print("A distancia entre os pontos é de {}, portanto é parametrizado como sendo:".format(distancia))

if(distancia >= 10):
    print("longe")
else:
    print("perto")