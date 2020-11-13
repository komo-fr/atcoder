#!/usr/bin/env python3
N = int(input())
import collections

s = input()
s_list = list(s)
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
print("aaaaaa")
print(f"{count_left=} {count_right=}")

for _ in range(count_left):
    s = s.replace(".#", "##")
for _ in range(count_right):
    s = s.replace("#.", "##")

count = collections.Counter(s)["."]

ans = f"{count_left + count} {count_right}"
print(ans)
