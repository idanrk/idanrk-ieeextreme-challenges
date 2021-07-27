t=int(input())
for _ in range(t):
    n=int(input())
    calc = n
    count=0
    while(calc>0):
        calc=calc//2
        count+=1
    distance_from_last_reset= n - ((2**(count-1)-1))
    print(distance_from_last_reset*2 - 1)