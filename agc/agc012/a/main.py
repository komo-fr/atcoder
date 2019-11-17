#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
a_list = sorted(a_list, reverse=True)

# N組できる
x_list = a_list[: 2 * N]
ans = sum([x for i, x in enumerate(x_list) if i % 2 == 1])

print(ans)
