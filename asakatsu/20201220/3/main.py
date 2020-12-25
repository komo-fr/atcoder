#!/usr/bin/env python3

S = input()
is_b = False
is_w = False
exists_w = False
exists_b = False
b_count = 0
w_count = 0
# 区間の数
for char in S:
    if is_b and char == "W":
        is_b = False
    elif not is_b and char == "B":
        is_b = True
        b_count += 2

    if is_w and char == "B":
        is_w = False
    elif not is_w and char == "W":
        is_w = True
        w_count += 2
    if char == "W":
        exists_w = True
    else:
        exists_b = True

# print(f"{b_count=}, {w_count=}")
if S[0] == "B":
    b_count -= 1
if len(S) != 1 and S[-1] == "B":
    b_count -= 1

if S[0] == "W":
    w_count -= 1
if len(S) != 1 and S[-1] == "W":
    w_count -= 1

count = min([w_count, b_count])
if not exists_w or not exists_b:
    count = 0

ans = count
print(ans)
