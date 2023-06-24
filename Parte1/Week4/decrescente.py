
decrescente = True
valor = 1;

anterior = int(input("Digite o primeiro número da sequencia:"))

while (valor != 0):
    valor = int(input("Digite o proximo número da sequencia:"))
    if valor > anterior:
        decrescente = False
    anterior = valor

if(decrescente == True):
    print("A sequencia está em ordem decrescente!")
else:
    print("A sequencia não está em ordem decrescente!")

    
