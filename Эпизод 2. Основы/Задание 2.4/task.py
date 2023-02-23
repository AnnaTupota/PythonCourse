def task_1(str):
    a={}
    for i in str:
        if i.isalpha():
            if i.lower() in a:
                a[i.lower()] += 1
            else:
                a[i.lower()] = 1
    return a


def task_2(list):

    return sum(set(list))


def task_3(cities):
    cities1 = ', '.join(cities)
    cities1 = cities1+"."
    return cities1


def task_4(a, b):
    result = list(set(a) & set(b))
    return result
