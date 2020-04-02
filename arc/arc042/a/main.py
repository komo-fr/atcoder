#!/usr/bin/env python3

N, M = list(map(int, input().split()))  # 10**5, 10**5
a_list = []

for _ in range(M):
    a = int(input().split()[0])
    a_list.append(a)

done_dict = {k: False for k in range(1, N + 1)}  # 10 ** 5
now_list = []

for a in a_list[::-1]:  # 10 ** 5
    if done_dict[a]:
        continue

    now_list.append(a)
    done_dict[a] = True

for k in range(1, N + 1):  # 10 ** 5
    if done_dict[k]:
        continue

    now_list.append(k)

ans = "\n".join([str(a) for a in now_list])

print(ans)
