import math
# Пример 1
def task_1(n):
    x = 0
    for i in range(1, n + 1):
        x += 1 / i
    return x


# Пример 2
def task_2(x, n):
    x = 0
    y = 1
    for i in range(1, n + 1, 2):
        x += y / i
    return x


# Пример 3
def task_3(n):
    x = math.factorial(n)
    return x


# Пример 4
def task_4(x, n):
    x = 1
    y = 1
    for i in range(2, n + 1):
        x *= (y + i) / i
    return x


# Пример 5
def task_5(x, n):
    x = 0
    y = 1
    for i in range(1, n + 1):
        x += (y * i) / (2 * i)
    return x


# Пример 6
def task_6(n):
    z = 1
    for i in range(2, n + 2, 2):
        z *= i
    return z
    return z
