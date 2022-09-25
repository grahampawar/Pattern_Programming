def pattern(n):
    for i in range(n):
        for j in range(1,n+1):
            print(j, end=" ")
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