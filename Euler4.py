#4. Palindrome Product

def reverseNumber(value):
    reversed = 0
    value = abs(value)
    while value > 0:
        digit = value % 10  #takes modulus of decimal, isolating LSB in base 10
        reversed = reversed * 10 + digit
        value = value//10   #shift to compensate
    return reversed

def isPalindrome(value):
    if (value == (reverseNumber(value))):
        return True
    else:
        return False

def findProducts():
    maxValue = 0
    tempValue = 0
    for i in range(100,1000): #stops at 99
        for j in range(100,1000):
            tempValue = i * j
            if(isPalindrome(tempValue) == True):
                #print(tempValue, "Is Palindrome")
                if (tempValue > maxValue):
                    maxValue = tempValue
    return maxValue



print("------")
print(findProducts())