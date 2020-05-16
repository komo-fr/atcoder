#!/usr/bin/env python3

K = int(input().split()[0])
A, B = list(map(int, input().split()))
is_ok = False
for i in range(A, B + 1):
    if i % K == 0:
        is_ok = True
        break
ans = "OK" if is_ok else "NG"
print(ans)
