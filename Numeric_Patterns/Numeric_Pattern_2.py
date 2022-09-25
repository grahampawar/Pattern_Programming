def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end =" ")
        print()

def inp():
    while True:
        try:
            num = int(input("Please enter a Non-zero,Positive Integer: "))
            if num <= 0 :
                while num <= 0:
                    num = int(input("Please enter a Non-zero,Positive Integer: "))
        except ValueError:
            continue
        else:
            break
    return num


no = inp()
pattern(no)