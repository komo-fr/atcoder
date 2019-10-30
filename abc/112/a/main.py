#!/usr/bin/env python3

N = int(input().split()[0])

if N == 1:
    ans = "Hello World"
else:
    A = int(input().split()[0])
    B = int(input().split()[0])
    ans = A + B

print(ans)
