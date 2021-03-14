#!/usr/bin/env python3

V, T, S, D = list(map(int, input().split()))

ans = "No" if V * T <= D <= V * S else "Yes"
print(ans)
