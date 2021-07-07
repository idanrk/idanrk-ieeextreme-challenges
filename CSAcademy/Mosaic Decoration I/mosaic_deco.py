#Challenge Link: https://csacademy.com/ieeextreme-practice/task/mosaic1/
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
import math

n = get_number()
c_b=get_number()
c_p=get_number()
black_sum=0
pink_sum=0
for _ in range(n): #running over n bathrooms
    black_sum+=get_number()
    pink_sum+=get_number()
print(math.ceil(black_sum/10)*c_b+math.ceil(pink_sum/10)*c_p)
exit(0)