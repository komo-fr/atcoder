#!/usr/bin/env python3

N = int(input().split()[0])
S = input()

ans = "Yes" if S[N - 1] == "o" else "No"

print(ans)
