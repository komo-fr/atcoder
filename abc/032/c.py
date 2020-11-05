# https://atcoder.jp/contests/abc032/tasks/abc032_c
# C - 列

N, K = list(map(int, input().split()))
s_list = []

for _ in range(N):
    s = int(input().split()[0])
    s_list.append(s)

max_l = 0
reach_right_flag = False
# 尺取り法
if 0 in s_list:
    max_l = N
else:
    w = 1
    start_index = 0
    for i in range(0, N):
        w *= s_list[i]

        if w > K:
            # 基準値を超えたので、これ以上は伸ばせない
            w //= s_list[start_index] # 最初にかけた分を取り消す
            start_index += 1
        max_l = max(max_l, i - start_index + 1)

print(max_l)