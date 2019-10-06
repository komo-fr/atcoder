# https://atcoder.jp/contests/abc140/tasks/abc140_d
# D - Face Produces Unhappiness
import bisect
N, K = list(map(int, input().split()))
S = input().split()[0]

p = 0
lr_index_list = []
rl_index_list = []
for i in range(1, N):
    if S[i] == S[i-1]:
        p += 1
    if S[i-1] + S[i] == 'LR':
        lr_index_list.append(i-1)
    if S[i-1] + S[i] == 'RL':
        rl_index_list.append(i-1)

n_lr = len(lr_index_list)
n_rl = len(rl_index_list)

if n_lr == 0 and n_rl == 0:
    pass
elif n_lr == 1 and n_rl == 0:
    if lr_index_list[0] != 0 and lr_index_list[0] != N - 2:
        # LLLLLRRRRR 系
        p = N - 1
elif n_lr == 0 and n_rl == 1:
    if rl_index_list[0] != 0 and rl_index_list[0] != N - 2:
        # RRRRRLLLLL 系
        p = N - 1
else:
    kouho_n = min(n_lr, n_rl)
    # 少ない方を基準で探す
    if kouho_n == n_lr:
        x_list = lr_index_list
        org_x_list = x_list[:]
        y_list = rl_index_list
        org_y_list = y_list[:]
    else:
        x_list = rl_index_list
        org_x_list = x_list[:]
        y_list = lr_index_list
        org_y_list = y_list[:]
    c = 0
    for x in org_x_list:
        y_index = bisect.bisect_left(y_list, x)
        is_ok = False
        # 1個右隣をチェック
        if y_index != len(y_list):
            if abs(y_list[y_index] - x) >= 2:
                is_ok = True
                y_list.remove(y_list[y_index])
                x_list.remove(x)
        # 1個左隣をチェック
        if is_ok == False and y_index != 0:
            if abs(y_list[y_index-1] - x) >= 2:  # TODO
                is_ok = True
                y_list.remove(y_list[y_index-1])
                x_list.remove(x)
        # 2個右隣があるかどうかをチェック
        if is_ok == False and y_index + 1 < len(y_list):
            is_ok = True
            y_list.remove(y_list[y_index+1])
            x_list.remove(x)
        # 2個左隣があるかどうかをチェック
        if is_ok == False and y_index - 2 >= 0:  # TODO
            is_ok = True
            y_list.remove(y_list[y_index-2])
            x_list.remove(x)
        if is_ok:
            c += 1
        if c >= K:
            break

    p += min(c, K) * 2

    w_list = x_list + y_list
    if 0 in w_list:
        w_list.remove(0)
    if N - 1 in w_list:
        w_list.remove(N-1)

    if K - c >= 1 and w_list:
        p += 1

ans = p
print(ans)
