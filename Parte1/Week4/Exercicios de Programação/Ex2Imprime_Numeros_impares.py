# Receba um número inteiro positivo na entrada e imprima os  n primeiros números ímpares naturais.  

i = int(input("Digite o valor de n: "))
vezes = 1
numero = 1

while(vezes < i):
    print(numero)
    
    vezes = vezes + 1
    numero = numero + 2

print(numero)


    