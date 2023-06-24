
def fizzBuzz(n):
    if((n % 3 == 0) and (n % 5 != 0)):
        return "Fizz"
    
    elif((n % 3 != 0) and (n % 5 == 0)):
        return "Buzz"
    
    elif((n % 3 == 0) and (n % 5 == 0)):
        return "FizzBuzz"
    
    else:
        return n
    
# print(fizzBuzz(5))
# print(fizzBuzz(15))
# print(fizzBuzz(3))
# print(fizzBuzz(4))
    
    