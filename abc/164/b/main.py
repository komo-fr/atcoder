#!/usr/bin/env python3

A, B, C, D = list(map(int, input().split()))
a = A
c = C
is_t = True
while True:
    c -= B
    if c <= 0:
        break
    a -= D
    if a <= 0:
        is_t = False
        break
ans = "Yes" if is_t else "No"
print(ans)
