#https://www.hackerrank.com/contests/ieeextreme-challenges/challenges/car-spark
t=int(input())
for _ in range(t):
    n=int(input())
    cars=[]
    for _ in range(n):
        start,end,value=map(int,input().split())
        cars.append((start,end,value))
    cars.sort(key=lambda f: (f[1],f[0]))
    dp=[0 for _ in range(50)]
    for i in range(n):
        j=cars[i][0]
        while j>=0:
            dp[cars[i][1]]=max(dp[cars[i][1]], dp[j] + cars[i][2]) # what's more valuable for d[end-time]? what's already found or this car, best valuable start plus the value of the end time..
            j-=1
    print(max(dp))