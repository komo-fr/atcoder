#!/usr/bin/env python3


a, b, c, d = list(map(int, input().split()))
e = min([a + b - c, d])
e = max([e, 0])

ans = e
print(ans)
