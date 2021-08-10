def fun(*a):
    sm = 0; pr = 1
    for i in range(len(a)):
        sm = sm+a[i]
        pr = pr*a[i]
    print("Sum is=", sm)
    print("Product is= ", pr)

fun(10, 12, 30, 40, 50, 60, 70, 80, 100, 50, 30, 10)