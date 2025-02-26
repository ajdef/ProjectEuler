import math

def factor(value):
    factorList = []
    for n in range(2, int(math.sqrt(value))):   #only check up to sqrt, as that will be where prime factors may lie
        if (value % n == 0):    
            factorList.append(n)
    return factorList

def isPrime(value):
    if value > 1:
        for i in range(2, (value//2)+1):    #check halfway, accounts for /2
            if (value%i) == 0:
                return False
        return True
    else:
        return False


    
factorList=factor(600851475143)
#factorList = factor(13195)
print(factorList)

for element in factorList:
    if(isPrime(element)):
        print("prime", element)



