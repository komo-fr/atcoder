#!/usr/bin/env python3

N = int(input().split()[0])
count = 0
for i in range(1, N + 1):
    if "7" not in str(i) and "7" not in str(oct(i)):
        count += 1
ans = count
print(ans)
