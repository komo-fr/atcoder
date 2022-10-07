#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
max_mikan = 0
for i in range(N):
    x = a_list[i]
    total_mikan = 0
    l = None
    r = i
    # print(f"{x=}, {total_mikan=}")
    for j in range(N):
        if j <= i:
            # 左側
            if a_list[j] >= x:
                # 食べられる
                l = j
                total_mikan += x
                # print(f"{j=}, a={a_list[j]}, {total_mikan=}")
                
            else:
                # 食べられないので左端をリセット
                total_mikan = 0
        else:
            # 右側
            if a_list[j] >= x:
                r = j
                total_mikan += x
                # print(f"{j=}, a={a_list[j]}, {total_mikan=}")
                
            else:
                break
        
    max_mikan = max([max_mikan, total_mikan])
    # print(f"{(l, r, x)} -> {total_mikan}")


ans = max_mikan
print(ans)
