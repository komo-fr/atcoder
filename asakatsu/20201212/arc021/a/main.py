#!/usr/bin/env python3

a_table = []
for _ in range(4):
    a_list = list(map(int, input().split()))
    a_table.append(a_list)
is_ok = False
for i, a_list in enumerate(a_table):
    for j in range(3):
        if a_list[j] == a_list[j + 1]:
            is_ok = True
            break
    if is_ok:
        break

a_table = list(zip(*a_table))

for i, a_list in enumerate(a_table):
    for j in range(3):
        if a_list[j] == a_list[j + 1]:
            is_ok = True
            break
    if is_ok:
        break
ans = "CONTINUE" if is_ok else "GAMEOVER"
print(ans)
