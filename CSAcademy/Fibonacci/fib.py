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
""" i tried the normal way.. time for the big guns..
from collections import deque
t = get_number()
fib=deque()
fib.append(1)
fib.append(2)
for _ in range(t):
    m=get_number()
    N=len(fib)
    if m<2:
        print(fib[m-1])
        continue
    for i in range(N,m):
        fib.append(fib[i-1]+fib[i-2])
    print(fib[m-1] % 10)"""
# i knew about this formula, took it from: https://stackoverflow.com/questions/61865607/improving-implementation-of-binets-formula-for-finding-nth-fibonacci-number-in
import math

def fib(n):
     
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)
         
    return F[0][0]
     
def multiply(F, M):
     
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])
     
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w
         
# Optimized version of
# power() in method 4
def power(F, n):
 
    if( n == 0 or n == 1):
        return;
    M = [[1, 1],
         [1, 0]];
         
    power(F, n // 2)
    multiply(F, F)
         
    if (n % 2 != 0):
        multiply(F, M)
    F[0][0] %=10
    F[0][1] %=10
    F[1][0] %=10
    F[1][1] %=10
    
t = get_number()
for _ in range(t):
    m=get_number()
    print(fib(m+1)%10)