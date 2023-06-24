"""
Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro 
e devolve o maior número primo menor ou igual ao número passado à função
"""

def ehPrimo(k):
    if k < 2:
        return False
    i = 2
    while i*i <= k:
        if k % i == 0:
            return False
        i += 1
    return True

def maior_primo(n):
    while n >= 2:
        if ehPrimo(n):
            return n
        n -= 1
    return None

# print(maior_primo(100))
# print(maior_primo(7))
        
        
    