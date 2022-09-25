def pattern(n):
    for i in range(1,n+1,1):
        for j in range(n,i,-1):
            print(" ", end=" ")

        for k in range(1,i+1):
            print(k, end = " ")

        for l in range(k,0,-1):
            print(l, end = " ")
        print()

def inp():
    while True:
        try:
            num = int(input("Enter a Non-Zero, Positive Integer: "))
            if num <= 0:
                while num <= 0:
                    num = int(input("Enter a Non-Zero, Positive Integer: "))
        except ValueError:
            continue
        else:
            break
    return num

pattern(inp())