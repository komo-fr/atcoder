#!/usr/bin/env python3

N, A, B = list(map(int, input().split()))
S = input()
k = 0
ans = ""
b_i = 0
for i, ch in enumerate(S):

    if ch == "b":
        b_i += 1
    r = "No"
    if ch == "a" and k < A + B:
        r = "Yes"
        k += 1
    elif ch == "b" and k < A + B and b_i <= B:
        r = "Yes"
        k += 1
    ans += r + "\n"

print(ans)
