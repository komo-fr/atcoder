#!/usr/bin/env python3

N = int(input().split()[0])
S = str(N)
a_list = []
b_list = []
total = 0
if int(S[0]) == 1 and int(S[1:]) == 0:
    total = 10
else:
    for char in S:
        total += int(char)

ans = total

print(ans)
