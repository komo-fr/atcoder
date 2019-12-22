#!/usr/bin/env python3

a = int(input().split()[0])
b = int(input().split()[0])
ans = set([1, 2, 3]) - set([a, b])
ans = list(ans)[0]

print(ans)
