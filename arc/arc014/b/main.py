#!/usr/bin/env python3

N = int(input().split()[0])
w_list = []
r = "DRAW"

for i in range(N):
    w = input()
    if i == 0:
        w_list.append(w)
        continue

    if w[0] != w_list[i - 1][-1] or w in w_list:
        if i % 2 == 0:
            r = "LOSE"
        else:
            r = "WIN"
        break
    w_list.append(w)
ans = r
print(ans)
