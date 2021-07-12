# https://www.hackerrank.com/contests/ieeextreme-challenges/challenges/game-of-stones-1-1
t=int(input())
for _ in range(t):
    g=int(input())
    total_piles=[]
    for _ in range(g):
        _=int(input())#i dont care about the length of the pile..
        total_piles.extend(map(int,(input().split())))
    turns=0
    for pile in total_piles:
        turns+=pile//2 #needs to figure out that each odd number has it own number of turns to break it to 1..
    if turns%2==0:
        print("Bob")
    else:
        print("Alice")