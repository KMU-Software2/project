import time

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


def iterfibo(n):
    if n <= 1:
        return n
    else:
        num_1 = 0                   # 'num_1' is iterfibo(n-2).
        num_2 = 1                   # 'num_2' is iterfibo(n-1).
        for i in range(n - 1):
            num_1, num_2 = num_2, num_1 + num_2
        return num_2


while True:
    nbr = int(input("Enter a number: "))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("iteribo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
