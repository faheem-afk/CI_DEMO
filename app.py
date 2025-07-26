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


result1 = add(4, 5)
result2 = sub(4, 1)
print(result1, result2)
