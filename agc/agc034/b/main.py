#!/usr/bin/env python3

s = input()
S = list(s)
N = len(S)
count = 0

for i in range(N - 2):
    sub_s = S[i] + S[i + 1] + S[i + 2]
    if sub_s == "ABC":
        S[i] = "B"
        S[i + 1] = "C"
        S[i + 2] = "A"
        count += 1

S = list(reversed(S))
for i in range(N - 2):
    sub_s = S[i + 2] + S[i + 1] + S[i]
    if sub_s == "ABC":
        S[i + 2] = "B"
        S[i + 1] = "C"
        S[i] = "A"
        count += 1
ans = count
print(ans)
