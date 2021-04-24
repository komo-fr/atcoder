#!/usr/bin/env python3

N, L, T, X = list(map(int, input().split()))
ab_list = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))

time_count = 0
over_time = 0
is_ok = True
for i, ab in enumerate(ab_list):
    a, b = ab
    if b >= L:
        # 過負荷
        if a > T:
            is_ok = False
            break
        if over_time + a < T:
            # 止まらずに完遂できる
            over_time += a  # そのまま追加
            time_count += a
        elif over_time + a == T:
            # 完遂した後にちょうど止まる
            over_time = 0  # リセット
            time_count += a + X  # 待ち時間つき
        else:
            # 停止して最初からやり直す必要がある
            additional_x = T - over_time  # 無駄に進んだ分
            over_time = a  # 一旦リセット
            time_count += a + X + additional_x
            if a == T:
                # ぴったりの場合、さらに追加でいる
                over_time = 0
                time_count += X
    else:
        # 過負荷ではない
        over_time = 0
        time_count += a

ans = time_count if is_ok else "forever"
print(ans)
