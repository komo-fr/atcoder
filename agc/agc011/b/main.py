#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
a_list = list(sorted(a_list))

c = 0
total_size = sum(a_list)

if N != 2:
    for i, a in enumerate(a_list):
        # 最終的に勝たないといけないモンスター
        last_size = a_list[-2] if i == N - 1 else a_list[-1]
        size = total_size - last_size
        if last_size <= size * 2:
            c += 1
else:
    a, b = a_list[0], a_list[1]
    if a <= b * 2 and b <= a * 2:
        c = 2
    elif a <= b * 2 or b <= a * 2:
        c = 1
    else:
        c = 0
ans = c
print(ans)
