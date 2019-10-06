#!/usr/bin/env python3

N, M = list(map(int, input().split()))
abc_list = []
counter = {i+1: [] for i in range(N)}

for i in range(M):
    a, b = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    abc_list.append((a, b, c_list))
    for c in c_list:
        # 宝箱を開けられる鍵のリスト
        counter[c] += [i+1]

for 




print(ans)
