def Pattern(n):
    for i in range(n+1):
        for s in range(i+1):
            print(" ", end = " ")
        for j in range(n,i,-1):
            print(j, end = " ")
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


Pattern(inp())