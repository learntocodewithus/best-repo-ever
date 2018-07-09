def triangle(n):
    for i in range(1, n+1):
        print("*" * i)

    for x in range(n-1, 0, -1):
        print("*" * x)

triangle(6)