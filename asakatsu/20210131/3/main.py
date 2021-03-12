#!/usr/bin/env python3

K, S = list(map(int, input().split()))
count = 0
for x in range(K + 1):
    for y in range(K + 1):
        z = S - (x + y)
        if 0 <= z <= K:
            count += 1

ans = count
print(ans)
