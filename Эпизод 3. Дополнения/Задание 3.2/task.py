import math
def task_1(A, a):
    A.sort
    low = 0
    high = len(A) - 1
    mid = len(A)//2

    while A[mid]!=a and low<=high:
        if a>A[mid]:
            low=mid+1
        else:
            high=mid-1
        mid = (low +high)// 2
    return str(mid)



def task_2(a):
    k=0
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k + 1
    if (k == 0):
        return True
    else:
        return False