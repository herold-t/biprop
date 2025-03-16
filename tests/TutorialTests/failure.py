def fibo(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
    return a


for i in range(10):
    if fibo(i) == 21:
        raise ValueError('Found illegal Fibonacci number!')