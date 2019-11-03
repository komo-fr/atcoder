#!/usr/bin/env python3

N, A, B = list(map(int, input().split()))

if A > B:
    ans = 0
elif N == 1:
    ans = 1 if A == B else 0
else:
    min_total = A * (N - 1) + B
    max_total = B * (N - 1) + A
    ans = max_total - min_total + 1

print(ans)
