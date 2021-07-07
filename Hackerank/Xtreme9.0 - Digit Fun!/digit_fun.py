#Challenge link: https://www.hackerrank.com/contests/ieeextreme-challenges/challenges/digit-fun
val = str(input())  # input=str
while (val != "END"):
    ctr = 1
    str_len = str(len(val))
    while (str_len != val):
        ctr += 1
        val = str_len
        str_len = str(len(val))
    print(ctr)
    val = str(input())
