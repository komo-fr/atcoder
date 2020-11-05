#!/usr/bin/env python3

N = int(input().split()[0])
ng_list = []

for _ in range(3):
    ng = int(input().split()[0])
    ng_list.append(ng)

c = 0
i = N
is_ok = True

if N in ng_list or 0 in ng_list:
    is_ok = False
else:
    while True:
        c += 1

        if c > 100:
            is_ok = False
            break

        if i - 3 >= 0 and i - 3 not in ng_list:
            i -= 3
        elif i - 2 >= 0 and i - 2 not in ng_list:
            i -= 2
        elif i - 1 >= 0 and i - 1 not in ng_list:
            i -= 1
        else:
            is_ok = False
            break

        if i == 0:
            break

ans = "YES" if is_ok else "NO"
print(ans)
