#!/usr/bin/env python3

N = int(input().split()[0])
xyh_list = []
not_zero_h_list = []

for _ in range(N):
    x, y, h = list(map(int, input().split()))
    xyh_list.append((x, y, h))
    if h != 0:
        not_zero_h_list.append((x, y, h))

# 高さ0の情報は除く
target_x, target_y, target_h = not_zero_h_list[0]

for cx in range(0, 101):
    for cy in range(0, 101):
        # cx, cy = 2, 2
        H_list = []
        # 基準
        H = target_h + abs(target_x - cx) + abs(target_y - cy)
        H = max(0, H)
        is_ok = True

        # 他の座標の結果と一致するかどうか確認する
        for x, y, h in xyh_list:  # ここが問題
            if h == 0:
                if (H - abs(x - cx) - abs(y - cy)) <= 0:
                    continue
                else:
                    # 一致しない
                    is_ok = False
                    break
            else:
                HH = h + abs(x - cx) + abs(y - cy)
                HH = max(0, HH)
                if HH != H:
                    # 一致しない
                    is_ok = False
                    break
        if is_ok:
            break

    if is_ok:
        break
ans = "{} {} {}".format(cx, cy, H)
print(ans)
