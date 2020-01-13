#!/usr/bin/env python3

k, x = list(map(int, input().split()))
ans = "Yes" if 500 * k >= x else "No"

print(ans)
