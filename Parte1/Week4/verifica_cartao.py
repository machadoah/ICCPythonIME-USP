meu_cartao = int(input("Digite o número do seu cartão de crédito: "))

cartao_lido = 1
encontrei_meu_cartao = False

while (cartao_lido != 0 and (encontrei_meu_cartao == False)):
    cartao_lido = int(input("Digite o número do próximo cartão de crédito: "))
    if (cartao_lido == meu_cartao):
        encontrei_meu_cartao = True

if (encontrei_meu_cartao == True):
    print("EBA!!! Meu cartão está lá!")
else:
    print("Xi, meu cartão não está lá...")