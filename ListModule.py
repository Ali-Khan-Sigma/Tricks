
simpleList = [11, 2, 33, 44, 55, 66, 77, 88, 99, 99, 99, 99]
listRange = list(range(0, 24, 2))


def loopMethod():
    i=0
    for x in listRange:
       if i<=7:
        print(x)
        i += 1

    print("totall %d"%i)

