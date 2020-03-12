#!/usr/bin/env python3

n, a, b = list(map(int, input().split()))
c = a + b
x = n // c
y = n % c

ans = a * x + min(a, y)
print(ans)
