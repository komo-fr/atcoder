#!/usr/bin/env python3
X = int(input().split()[0])
x = 100
count = 0
while x < X:
    x += x // 100
    count += 1

ans = count
print(ans)
