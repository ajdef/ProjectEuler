#5. Smallest Multiple
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
counter = 0
smallest = 0
for i in range(19, 99999999999, 19):
    for j in range(1,21):   #1-10
        if (i % j == 0):    #if evenly divisible by j
            counter += 1
        else:
            counter = 0
            break
    if (counter == 20):
        print(i)
        break


