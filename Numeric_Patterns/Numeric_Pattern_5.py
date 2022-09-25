def pattern(n):
    for i in range(n):
        for s in range(n-i-1):
            print(" ",end = " ")
        
        for j in range((i*2)+1):
            print(j+1, end =" ")
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