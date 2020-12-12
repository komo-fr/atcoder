#!/usr/bin/env python3

a, b, c = list(map(int, input().split()))

ans = len(set([a, b, c]))
print(ans)
