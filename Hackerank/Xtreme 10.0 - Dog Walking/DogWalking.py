# https://www.hackerrank.com/contests/ieeextreme-challenges/challenges/dog-walking/problem
t = int(input())
for _ in range(t):
    dogs=[]
    ranges=[]
    N,K=map(int,input().split())
    if N==1 or N/K==1:
        print(0)
        continue
    for _ in range(N):
        dogs.append(int(input()))
    dogs.sort()
    if K==1:
        print(dogs[-1]-dogs[0])
        continue
    for i in range(1,N):
        ranges.append(dogs[i]-dogs[i-1])
    ranges.sort()
    max_range=dogs[-1]-dogs[0]
    #we'll put the highest dogs with single dogwalker so the range will be 
    high=sum(ranges[-(K-1):]) #say we have 4 dog-walkers. 3 with single dog. 1 with the rest
    print(max_range-high)