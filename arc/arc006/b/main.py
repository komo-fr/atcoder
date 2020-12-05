#!/usr/bin/env python3

N, L = list(map(int, input().split()))
amida_list = []
for _ in range(L + 1):
    row = input()
    amida_list.append(row)

col_n = 2 * N - 1

for i, row in enumerate(amida_list[::-1]):
    if i == 0:
        now_index = row.index("o")
        # print(f"{i}, {now_index=}")
        continue
    r_index = now_index + 1
    l_index = now_index - 1

    if now_index < col_n - 1 and row[r_index] == "-":
        now_index += 2
    elif now_index > 0 and row[l_index] == "-":
        now_index -= 2
    # print(f"{i}, {now_index=}")
ans = now_index // 2 + 1
print(ans)
