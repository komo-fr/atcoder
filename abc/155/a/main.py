#!/usr/bin/env python3

a, b, c = list(map(int, input().split()))

if len(set([a, b, c])) == 1:
    ans = "No"
elif len(set([a, b, c])) == 2:
    ans = "Yes"
else:
    ans = "No"

print(ans)
