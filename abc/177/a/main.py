#!/usr/bin/env python3
D, T, S = list(map(int, input().split()))

ans = "Yes" if D / S <= T else "No"

print(ans)
