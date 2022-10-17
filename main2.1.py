def triangle():
    a = int (input())
    base = a*2+1
    kol = 1
    for i in range(a+1):
        print(" " * a, end="")
        print("*" * kol)
        kol = kol+2
        a = a-1


triangle()