#!/usr/bin/env python3

N = int(input().split()[0])

s = sum([int(i) for i in str(N)])
ans = "Yes" if N % s == 0 else "No"

print(ans)
