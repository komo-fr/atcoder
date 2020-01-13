#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
a_list = list(sorted(a_list))

win_c = 0
total_size = sum(a_list)
max_size_list = []

if N != 2:
    lose_flag = False
    now_size = 0
    first_winner = -1
    for i, a in enumerate(a_list):
        if i == N - 1:
            break
        # 確実に倒せるやつはどいつか
        now_size += a
        if now_size * 2 >= a_list[i + 1]:
            # 勝てる
            if lose_flag:
                first_winner = i
                break
        else:
            lose_flag = True
    c = N if first_winner == -1 else N - first_winner
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
