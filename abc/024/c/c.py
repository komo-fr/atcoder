#!/usr/bin/env python3
N, D, K = list(map(int, input().split()))

lr_list = []
for _ in range(D):
    l, r = list(map(int, input().split()))
    lr_list.append((l, r))

st_list = []
for _ in range(K):
    s, t = list(map(int, input().split()))
    st_list.append((s, t))

day_list = []
for s, t in st_list:
    if s < t:
        direction = 'r'
    else:
        direction = 'l'
    now_x = s

    for i, lr in enumerate(lr_list):
        l, r = lr
        if l <= now_x <= r:
            # 進めるだけ進む
            now_x = r if direction == 'r' else l
            if (direction == 'r' and now_x >= t) or (direction == 'l' and now_x <= t):
                break

    day_list.append(str(i + 1))

ans = '\n'.join(day_list)
print(ans)
