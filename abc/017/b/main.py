#!/usr/bin/env python3

x = input()
x = "".join(list(reversed(x)))

while x:
    if x[0] in ["o", "k", "u"]:
        x = "" if len(x) == 1 else x[1:]
    elif len(x) >= 2 and x[:2] == "hc":
        x = "" if len(x) == 2 else x[2:]
    else:
        break

ans = "NO" if x else "YES"

print(ans)
