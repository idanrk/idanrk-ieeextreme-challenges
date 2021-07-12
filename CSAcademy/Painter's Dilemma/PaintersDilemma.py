# https://csacademy.com/ieeextreme-practice/task/painters-dilemma/
# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


# numpy and scipy are available for use
import numpy
import scipy

t = get_number()
for _ in range(t):
    n = get_number()
    cl = []
    b1 = 0
    b2 = 0
    faults = 0
    for _ in range(n):
        cl.append(get_number())
    for i in range(len(cl)):
        if cl[i] != b1 and cl[i] != b2:
            faults += 1
            if b1 not in cl[i + 1:]:
                b1 = cl[i]
            elif b2 not in cl[i + 1:]:
                b2 = cl[i]
            elif cl[i + 1:].index(b1) < cl[i + 1:].index(b2):
                b2 = cl[i]
            else:
                b1 = cl[i]
    print(faults)
