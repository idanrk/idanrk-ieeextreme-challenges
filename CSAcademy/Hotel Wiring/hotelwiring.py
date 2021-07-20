#https://csacademy.com/ieeextreme-practice/task/hotel-wiring/
t= int(input())
for _ in range(t):
    m,n,k=map(int,input().split())
    floor_wired=[]
    for _ in range(m):
        a=int(input())
        floor_wired.append(a)
    floor_wired.sort()
    for i in range(k):
        floor_wired[i]=n-floor_wired[i]
    print(sum(floor_wired))