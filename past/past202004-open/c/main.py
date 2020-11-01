#!/usr/bin/env python3

N = int(input().split()[0])
s_table = []

for _ in range(N):
    s = input()
    s_table.append(s)


for i in range(N - 1, -1, -1):
    if i == N - 1:
        continue
    start = (N - i) - 1
    end = N + i
    preset = "." * start
    t = preset

    for j in range(start, end):
        if (
            s_table[i + 1][j - 1] == "X"
            or s_table[i + 1][j] == "X"
            or s_table[i + 1][j + 1] == "X"
        ):
            # print("True")
            out = "X"
            t += "X"
        else:
            out = s_table[i][j]
            t += s_table[i][j]
        # print("================")
        # print(
        #     f"({i+1}, {j-1}), ({i+1}, {j}), ({i+1}, {j+1})------> {s_table[i+1][j-1]}{s_table[i+1][j]}{s_table[i+1][j+1]} -> {out}"
        # )

    t += preset
    s_table[i] = t

for s in s_table:
    print(s)