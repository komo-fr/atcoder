#!/usr/bin/env python3

a, b, x = list(map(int, input().split()))
a_n = a // x
b_n = b // x

ans = b_n - a_n
ans = ans + 1 if a % x == 0 else ans

print(ans)
