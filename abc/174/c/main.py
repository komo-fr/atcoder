#!/usr/bin/env python3

K = int(input().split()[0])
if K % 2 == 0:
    ans = -1
else:
    i = 1

    while (7 * int("1" * i)) % K != 0:
        i += 1
    ans = i

print(ans)
