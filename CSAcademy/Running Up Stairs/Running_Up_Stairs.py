#challenge link: https://csacademy.com/ieeextreme-practice/task/96c8b1313edd72abf600facb0a14dbab/statement/

# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

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
t = get_number()
for s in range(t):
    # fib secuence
    v1 = 1
    v2 = 1
    for _ in range(get_number()):
        v3 = v1 + v2
        v1 = v2
        v2 = v3
    print(v1)