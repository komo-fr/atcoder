#!/usr/bin/env python3
import fractions

a, b = list(map(int, input().split()))
ans = a * b // fractions.gcd(a, b)

print(ans)
