#!/usr/bin/env python3

N = int(input().split()[0])
n = sum([int(s) for s in str(N)])

ans = "Yes" if n % 9 == 0 else "No"
print(ans)
