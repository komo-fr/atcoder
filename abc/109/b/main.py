#!/usr/bin/env python3

N = int(input().split()[0])
w_list = []
is_ok = True
for i in range(N):
    w = input()

    if w in w_list:
        is_ok = False
        break

    w_list.append(w)
    if i == 0:
        tail = w[-1]
        continue

    if w[0] != tail:
        is_ok = False
        break
    tail = w[-1]


ans = "Yes" if is_ok else "No"
print(ans)
