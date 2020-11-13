#!/usr/bin/env python3
N = int(input())
import collections

S = input()
s_list = list(S)
count_left = 0
count_right = 0

for s in s_list:
    if s == ".":
        count_left += 1
    else:
        break

for s in reversed(s_list):
    if s == ".":
        count_right += 1
    else:
        break


for _ in range(count_left):
    S = S.replace(".#", "##")

for _ in range(count_right):
    S = S.replace("#.", "##")

count = collections.Counter(S)["."]
plus = 0
while count != 0:
    plus += 1
    if "#." in S:
        S = S.replace("#.", "##")
    else:
        S = S.replace(".#", "##")
    count = collections.Counter(S)["."]

ans = f"{count_left} {count_right+plus}"
print(ans)
