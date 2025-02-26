import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i == 0):
            return False
    return True

def nthPrime(n):
    primeCount = 0
    primeGoal = n
    lastPrime = 0
    for i in range(2, 105000):
        if (isPrime(i) == True):
            primeCount += 1
            lastPrime = i
            print(primeCount, " prime is:", i)
        if (primeCount > primeGoal-1):
            break
    return lastPrime



            



print(nthPrime(10001))
#for i in range(1,100):
 #   print(isPrime(i), i)