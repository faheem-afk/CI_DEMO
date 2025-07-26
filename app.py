def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a/b


def mod(a):
    if a < 0:
        return a * -1
    else:
        return a


def mul(a, b):
    return a * b


def root(a):
    return a**1/2


def root2(a):
    return a**1/2


def root4(a):
    return a**1/2


result1 = add(4, 5)
result2 = sub(4, 1)
print(result1, result2)
