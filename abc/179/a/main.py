#!/usr/bin/env python3

S = input()

ans = S + "s" if S[-1] != "s" else S + "es"
print(ans)
