def fatorial(n):
    fatorial = 1
    
    while(n > 0):
        fatorial = fatorial * n
        n = n - 1
        
    return fatorial

def binomio_newton(n, k):
    
    solucao = fatorial(n) / (fatorial(k) * fatorial(n - k))
    
    return solucao

n = int(input("Forneça o valor de n: "))
k = int(input("Forneca o valor de k: "))

print(binomio_newton(n, k))

