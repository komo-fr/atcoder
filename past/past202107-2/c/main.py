#!/usr/bin/env python3

S = input()
l, r = list(map(int, input().split()))

if S[0] == "0" and S != "0":
    ans = "No"
else:
    is_ok = "No"
    if len(S) > 10:
        ans = "No"
    else:
        if l <= int(S) <= r:
            ans = "Yes"
        else:
            ans = "No"

print(ans)
