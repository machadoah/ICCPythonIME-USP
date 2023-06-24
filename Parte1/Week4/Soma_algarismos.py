numero = int(input("Digite um numero inteiro: "))

soma = 0

while(numero != 0):
    soma = soma + (numero % 10)
    numero = numero // 10

print("A soma dos algarismos é:", soma)
    