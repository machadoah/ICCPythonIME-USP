soma = 0
print("Digite uma sequencia de valores, terminada em 0.")

valor = 1

while(valor != 0):
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor

print("A soma dos valores digitados é:", soma)