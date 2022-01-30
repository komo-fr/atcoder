#!/usr/bin/env python3

N = int(input().split()[0])
ok_list = []
for i in range(2, N // 2 + 1):
    for j in range(2, N // 2 + 1):
        if i ** j > N:
            break
        ok_list.append(i ** j)

ans = N - len(set(ok_list))
print(ans)
