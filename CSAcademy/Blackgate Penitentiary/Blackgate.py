#Challenge Link: https://csacademy.com/ieeextreme-practice/task/8761fb7efefcf1d890df1d8d91cae241/statement/
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

n = get_number()
heights = {}
for _ in range(n):
    name, height = get_word(), get_number()
    if height not in heights.keys():
        heights[height] = [name]
    else:
        heights[height].append(name)
heights = dict(sorted(heights.items()))
mini = 1
maxi=0
for val in heights.values():
    for name in sorted(val):
        print(name, end=' ')
        maxi+=1
    print(mini, maxi)
    mini=maxi+1