#!/usr/bin/env python3

N, K = list(map(int, input().split()))

x = N % K
done_list = [x]
min_x = x
while True:
    x = abs(x - K)
    done_list.append(x)
    min_x = min(x, min_x)
    if x in done_list:
        break
ans = min_x

print(ans)
