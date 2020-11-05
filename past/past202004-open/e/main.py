#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
x2ax_map = {}

for i, a in enumerate(a_list):
    x = i + 1
    x2ax_map[x] = a

# print(x2ax_map)

ans_list = []
for x in range(1, N + 1):
    # print(f"i={x}")
    # j = 1
    if x == x2ax_map[x]:
        j = 1
        ans_list.append(str(j))
        continue
    start_x = x
    j = 1
    while start_x != x2ax_map[x]:
        j += 1
        # print(f"[{j}] x, ax = ({x}, {x2ax_map[x]})")
        ax = x2ax_map[x]
        x = ax
    # j += 1
    ans_list.append(str(j))
ans = " ".join(ans_list)
print(ans)
