#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
b_list = [(i+1, a) for i, a in enumerate(a_list)]

while len(b_list) != 2:
    next_list = []
    n = len(b_list)
    for i in range(n//2):
        a = b_list[i*2]
        b = b_list[i*2+1]
        if a[1] >= b[1]:
            winner = a
        else:
            winner = b
        next_list.append(winner)
    b_list = next_list
else:
    a = b_list[0]
    b = b_list[1]
    if a[1] >= b[1]:
        loser = b
    else:
        loser = a

ans = loser[0]
print(ans)
