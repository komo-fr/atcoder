#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))

odd_n = len([a for a in a_list if a < 0])

# 負の数の個数が偶数の場合は、全部正にできる
if odd_n % 2 == 0:
    s = 0
    for a in a_list:
        s += abs(a)
else:
    # 負の数の個数が奇数の場合は、0があったら全部正にできる
    # 0がない場合は、どれか1個が負のままで残るので、絶対値が一番小さいものを残す
    s = 0
    if 0 in a_list:
        for a in a_list:
            s += abs(a)
    else:
        min_abs = float('inf')
        for a in a_list:
            s += abs(a)
            min_abs = min(min_abs, abs(a))
        s -= min_abs * 2

ans = s
print(ans)
