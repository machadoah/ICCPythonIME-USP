# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

numero = int(input("Digite um numero inteiro: "))
algarismo = 0

while(numero != 0):
    if(numero % 10 == (numero // 10) % 10):
        algarismo = algarismo + 1
    numero = numero // 10

if(algarismo > 0):
    print("sim")
else:
    print("não")