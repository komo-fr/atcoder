#!/usr/bin/env python3

N, M = list(map(int, input().split()))
b_table = []
is_ok = True
for _ in range(N):
    b_list = list(map(int, input().split()))
    b_table.append(b_list)

index = M % 7
if index == 0:
    start_list = [1]
else:
    start_list = list(range(1, 8))[: 8 - index]
    start_list = [x if x != 7 else 0 for x in start_list]

for i, b_list in enumerate(b_table):
    # print(f"{start_list=}")
    # print(f"{b_list[0] % 7 =}")
    if i == 0:
        if b_list[0] % 7 not in start_list:
            is_ok = False
            break
    else:
        if b_list[0] != b_table[i - 1][0] + 7:
            is_ok = False
            break

    for j, b in enumerate(b_list):
        if j == 0:
            continue
        if b != b_list[j - 1] + 1:
            is_ok = False
            break

ans = "Yes" if is_ok else "No"
print(ans)
