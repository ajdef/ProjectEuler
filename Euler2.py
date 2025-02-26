def evenFib(a, b, evenSum = 0):
    
    if (a > 4000000):   #reached once 4 million executions happen
        print(evenSum)
        return evenSum
    
    if (a%2 == 0):  #if even value
        evenSum += a    #add even value

    return evenFib(b, (b+a), evenSum)


evenFib(1,2)