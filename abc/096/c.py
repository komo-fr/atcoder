# https://atcoder.jp/contests/abc096/tasks/abc096_c
# C - Grid Repainting 2

h, w = list(map(int, input().split()))
s_list_list = []

for _ in range(h):
    s_list = list(input().split()[0])
    s_list_list.append(s_list)

done_list_list = [[False] * w for _ in range(h)]
is_ok = True

for h_i, s_list in enumerate(s_list_list):

    for w_i, s in enumerate(s_list):

        if s == '.':
            continue

        # 左から右、上から下に見ていく
        # 当該マスより左、上にある#は塗りつぶし済のはず

        # 右、下に#があったら優先的に塗りつぶす
        if h_i + 1 < h and s_list_list[h_i+1][w_i] == '#':
            done_list_list[h_i][w_i] = True
            done_list_list[h_i+1][w_i] = True

        if w_i + 1 < w and s_list_list[h_i][w_i+1] == '#':
            done_list_list[h_i][w_i] = True
            done_list_list[h_i][w_i+1] = True

        if not done_list_list[h_i][w_i]:
            is_ok = False
            break

    if not is_ok:
        break

ans = 'Yes' if is_ok else 'No'
print(ans)
