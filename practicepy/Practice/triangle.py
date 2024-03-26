def pyramid1(rows):
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ", end="")
        for j in range(i+1):
            print("*", end=" ")
        print()

pyramid1(5)


def pyramid2(rows):
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()

def pyramid3(rows):
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        print()

#pyramid3(5)
#pyramid2(5)
