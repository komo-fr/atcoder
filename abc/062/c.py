# https://atcoder.jp/contests/abc062/tasks/arc074_a?lang=ja
# C - Chocolate Bar

H, W = list(map(int, input().split()))
area = H * W

# 最初の長方形を決める
p_list = []
hw_list = [(H, W)]

if H != W:
    # 縦横入れ替えた場合の探索
    hw_list.append((W, H))

for hw in hw_list:
    h, w = hw
    for h_i in range(h):
        a_area = h_i * w
        # 残りの面積をなるべく均等に分ける
        # 残りを縦に割る場合
        h2, amari = divmod((h-h_i), 2)
        area_list = [a_area, h2*w, (h2+amari)*w]
        p_1 = max(area_list) - min(area_list)

        # 残りを横に割る場合
        w2, amari = divmod(w, 2)
        area_list = [a_area, (h-h_i)*w2, (h-h_i)*(w2+amari)]
        p_2 = max(area_list) - min(area_list)
        p_list.append(min(p_1, p_2))

ans = int(min(p_list))
print(ans)