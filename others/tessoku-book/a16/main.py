#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# iに到達するまでの最小コスト
# ・d_list[i-1] + a_list[i]
# ・d_list[i-2] + b_list[i]
# のうち、小さい方を採用する
d_list = []

for i in range(N):
    if i == 0:
        d_list = [0]
    elif i == 1:
        d_list.append(d_list[i - 1] + a_list[i - 1])
    else:
        a = d_list[i - 1] + a_list[i - 1]
        b = d_list[i - 2] + b_list[i - 2]
        d_list.append(min([a, b]))

ans = d_list[-1]
print(ans)
