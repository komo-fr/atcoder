#!/usr/bin/env python3

a, b = list(map(int, input().split()))
ans = list(sorted([str(a) * b, str(b) * a]))[0]
print(ans)
