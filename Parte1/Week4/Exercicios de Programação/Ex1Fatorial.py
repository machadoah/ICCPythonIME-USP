# Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.

numero = int(input("Digite o valor de n: "))

fatorial = 1

while(numero > 0): # enquanto o numero for maior que 0
    fatorial = fatorial * numero # fatorial recebe o valor de fatorial * numero
    numero = numero - 1 # numero recebe o valor de numero - 1

print(fatorial) # 120