numero = int(input("Digite um numero inteiro: "))
algarismo = 0

while(numero != 0):
    if(numero % 10 == (numero // 10) % 10):
        algarismo = algarismo + 1
    numero = numero // 10

if(algarismo > 0):
    print("sim, o numero tem algarismos adjacentes iguais")
else:
    print("não, o numero não tem algarismos adjacentes iguais")