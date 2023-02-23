# todo: replace this with an actual task
def task_1(str):
    a = []
    for i in str.split(' '):
        if i != ' ':
            a.append(i)


    return len(a[-1])


def task_2(str):
    a=[]
    for i in str.split(' '):
        if i != ' ':
            a.append(i)
    for d in range(0, len(a)-1, 2):
        a[d], a[d+1]=a[d+1], a[d]
    otvet =" ".join(a)

    return otvet


def task_3(str):
    a = str.split(' ')
    count=0

    for i in range(0, len(a)-1):
        if (a[i][-1]==a[i+1][0]):
            count+=1


    return count
