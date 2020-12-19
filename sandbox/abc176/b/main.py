#!/usr/bin/env python3

N = int(input().split()[0])

ans = "Yes" if sum([int(i) for i in str(N)]) % 9 == 0 else "No"
print(ans)
