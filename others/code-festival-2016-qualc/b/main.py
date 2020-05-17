#!/usr/bin/env python3

K, T = list(map(int, input().split()))
a_list = list(map(int, input().split()))
a_list = sorted(a_list)
k = K

if T == 1:
    count = K - 1
elif T == 2:
    diff = a_list[-1] - a_list[-2]
    if diff <= 1:
        count = 0
    else:
        count = diff - 1
else:
    # 一番多いケーキと2番目に多いケーキの個数の差
    diff = a_list[-1] - a_list[-2]
    if diff <= 1:
        count = 0
    else:
        x = sum(a_list[:-2])
        if (a_list[-1] - 1) <= (a_list[-2] + x):
            count = 0
        else:
            count = a_list[-1] - (a_list[-2] + x) - 1
ans = count
print(ans)
