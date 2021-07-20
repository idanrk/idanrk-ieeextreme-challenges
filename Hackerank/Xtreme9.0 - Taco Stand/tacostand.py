#https://www.hackerrank.com/contests/ieeextreme-challenges/challenges/taco-stand/submissions/code/1335257136
from math import floor
from statistics import median
n=int(input())
for _ in range(n):
    s, m, r, b=map(int,input().split())
    
    x = min(r, m, b) #the smallest quantity of all fillings
    y = median([r, m, b]) #the middle quantity of all fillings
    z = max(r, m, b) #the largest quantity of all fillings
    if z >( x + y):
        print(min(s, x + y))
    elif z <= (x + y):
        print(min(s, floor((x + y + z)/2)))