quantidade = int(input("Digite a quantidade de numeros que serão multiplicados: "))

i = 1
multiplicacao = 1

while(i <= quantidade):
    numero = int(input("Digite um numero: "))
    i = i + 1
    multiplicacao = multiplicacao * numero

print("A multiplicação dos numeros digitados é:", multiplicacao)