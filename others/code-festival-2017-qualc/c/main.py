#!/usr/bin/env python3

S = input()
N = len(S)
count = 0
is_ok = True

right_index = 0
left_index = N - 1

while right_index < left_index:

    if right_index == left_index:
        break

    if S[right_index] == S[left_index]:
        right_index += 1
        left_index -= 1
        continue
    if S[right_index] == "x":
        count += 1
        right_index += 1
        continue

    if S[left_index] == "x":
        count += 1
        left_index -= 1
        continue

    count = -1
    break

ans = count

print(ans)
