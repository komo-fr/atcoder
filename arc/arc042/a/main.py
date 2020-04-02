#!/usr/bin/env python3

N, M = list(map(int, input().split()))
a_list = []

for _ in range(M):
    a = int(input().split()[0])
    a_list.append(a)

now_list = [x for x in range(1, N + 1)]

for a in a_list:
    now_list.remove(a)
    now_list.insert(0, a)

ans = "\n".join([str(a) for a in now_list])

print(ans)
