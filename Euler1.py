def main():
    maxValue = range(1000)
    threeCount = 0
    fiveCount = 0
    bothCount = 0
    for n in maxValue:
        if((n%3 == 0) or (n%5 == 0)):
            bothCount = bothCount + n
    print(bothCount)


main()