#!/usr/bin/env python3

S = int(input().split()[0])
count = 0

if S in [1, 2]:
    ans = 0
elif S == 3:
    ans = 1
else:
    t_list = []
    for x in range(3, S + 1):
        for y in range(x, S + 1):
            z = S - (x + y)
            if z < 3:
                continue
            count += 1
            t_list.append(tuple(sorted(x, y, z)))
    ans = len(set(t_list))

print(ans)
