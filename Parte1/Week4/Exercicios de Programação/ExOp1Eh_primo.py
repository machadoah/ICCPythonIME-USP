# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

numero = int(input("Digite um número inteiro: "))
i = 2
primo = 0

while(numero > i):
    if(numero % i == 0):
        primo = primo + 1
    i = i + 1
    
if(primo == 0):
    print("primo")
else:
    print("não primo")