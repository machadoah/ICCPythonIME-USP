import math

def delta(a, b, c):
    
    delta =  math.pow(b,2) - 4 * a * c
    
    return delta

def raiz(a, b, c):
    
    if(delta(a, b, c) > 0):
        
        x1 = (- b + math.sqrt(delta(a, b, c))) / (2 * a)
        x2 = (- b - math.sqrt(delta(a, b, c))) / (2 * a)
        
        return print(x1, x2)
    
    elif (delta(a, b, c) == 0):
        
        x1 = (- b + math.sqrt(delta(a, b, c))) / (2 * a)
        
        return print(x1)
    
    else:
        print("Não existe raizes reais.")

def equacao_segundo_grau(a, b, c):
    
    return raiz(a, b, c)
        

a = float(input("Insira um valor para a: "))
b = float(input("Insira um valor para d: "))
c = float(input("Insira um valor para c: "))

equacao_segundo_grau(a, b, c)
        
    
    
    