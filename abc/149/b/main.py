#!/usr/bin/env python3

A, B, K = list(map(int, input().split()))
nokori = K
if A > 0:
    if K <= A:
        nokori = 0
        A = A - K
    else:
        nokori = K - A
        A = 0
if nokori > 0 and B > 0:
    if nokori <= B:
        B = B - nokori
        nokori = 0
    else:
        nokori -= B
        B = 0

ans = "{} {}".format(A, B)

print(ans)
