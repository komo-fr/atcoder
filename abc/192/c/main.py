#!/usr/bin/env python3

N, K = list(map(int, input().split()))
a = N
for _ in range(K):
    a_1 = int("".join(sorted(str(a))))
    a_2 = int("".join(sorted(str(a), reverse=True)))
    # print(f"{a_1=}, {a_2=}")
    a = a_2 - a_1

ans = a
print(ans)
