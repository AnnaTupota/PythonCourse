
import math
# Пример 1
def task_1(A):
    s = 0
    for i in range(len(A)):
        if A[i] > 0:
            s += A[i]
    return s


# Пример 2
def task_2(A):
    sr = sum(A) / len(A)
    return sr


# Пример 3
def task_3(A):
    sr_arif = sum(A) / len(A)
    sumsum = 0
    for i in range(len(A)):
        sumsum += ((A[i] - sr_arif) ** 2)
    otvet = (math.sqrt(sumsum / len(A)) )

    return otvet
