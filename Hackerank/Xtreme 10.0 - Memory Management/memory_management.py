#https://www.hackerrank.com/contests/ieeextreme-challenges/challenges/memory-management/problem

import math
from collections import deque
def page_num(address,s):
    return math.floor(address/s)

t=int(input())
for _ in range(t):
    ans=""
    p,s,n=map(int,input().split())
    fifo=deque()
    fifo_pf=0
    lru=deque()
    lru_pf=0
    for _ in range(n):
        page=page_num(int(input()),s)
        if page not in fifo:
            if len(fifo)==p:
                fifo_pf+=1
                fifo.popleft()
            fifo.append(page)
        if page not in lru:
            if len(lru)==p:
                lru_pf+=1
                lru.pop()
            lru.appendleft(page)
        else:
            lru.remove(page)
            lru.appendleft(page)
    if lru_pf<fifo_pf:
        print(f"yes {fifo_pf} {lru_pf}")
    else:
        print(f"no {fifo_pf} {lru_pf}")