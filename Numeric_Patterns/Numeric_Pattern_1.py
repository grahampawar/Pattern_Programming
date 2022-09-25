
# A function that returns a Pattern of Numbers in a Rigt - angled Triangle form.

def pattern(n):
    for i in range(n+1):
        for j in range(1,i+1):
            print(j, end = " ")
        print()

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

no = inp()
pattern(no)