#!/usr/bin/env python3

a, b, c = list(map(int, input().split()))

ans = "Yes" if a + b == c or b + c == a or c + a == b else "No"

print(ans)
