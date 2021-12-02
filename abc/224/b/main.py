#!/usr/bin/env python3

H, W = list(map(int, input().split()))
a_table = []

for _ in range(H):
    a_list = list(map(int, input().split()))
    a_table.append(a_list)

is_ok = True
for i_1 in range(H):
    for j_1 in range(W):
        for i_2 in range(i_1 + 1, H):
            for j_2 in range(j_1 + 1, W):
                x = a_table[i_1][j_1] + a_table[i_2][j_2]
                y = a_table[i_2][j_1] + a_table[i_1][j_2]
                if x > y:
                    is_ok = False
                    break
ans = "Yes" if is_ok else "No"
print(ans)
