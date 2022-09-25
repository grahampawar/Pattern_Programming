
# A function which returns a count of Positive integers from 1 to n.

def counting(n):
    for i in range(1, n+1):
        print(i, end=' ')




# A function which validates input to only accept Non - Zero, Positive Integers.

def inp():
    while True:
        try:
            num = int(input("Please enter a Non-zero,Positive Integer: "))
            if num<=0:
                while num<=0:
                    num = int(input("Please enter a Non-zero,Positive Integer: "))
        except ValueError:
            continue
        else:
            break
    return num

n = inp()
counting(n)