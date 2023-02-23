import math
def task_1(N):
    x=1
    for i in range(2, N+1):
       x *= i
    return x


def task_2(N):
    fib = int(((((1+math.sqrt(5))/2)**(N-1))-(((1-math.sqrt(5))/2)**(N-1)))/math.sqrt(5))
    return fib


def task_3(N):
    l = []
    if N > 0:
        for d in range(1, N + 1):
            if N % d == 0:
                l.append(d)
    return l
