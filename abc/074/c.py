# https://atcoder.jp/contests/abc074/tasks/arc083_a
# C - Sugar Water
import math
w_A, w_B, s_C, s_D, limit_E, max_F = list(map(int, input().split()))

# それ以上溶かすことができるか
# それ以上重量を増やせるか

# 取りうる水の組み合わせ
w_A_list = [w_A * x * 100 for x in range(math.floor(max_F / (w_A * 100)) + 1)]
w_B_list = [w_B * x * 100 for x in range(math.floor(max_F / (w_B * 100)) + 1)]

# 最悪で3000*3000
w_list = []
for a in w_A_list:
    for b in w_B_list:
        if a + b <= max_F:
            w_list.append(a + b)
w_list = list(set(w_list))  # 3000以下

# 取りうる水の組み合わせ
s_C_list = [s_C * x  for x in range(math.floor(max_F / s_C) + 1)]
s_D_list = [s_D * x  for x in range(math.floor(max_F / s_D) + 1)]

# 最悪で3000*3000
s_list = []
for c in s_C_list:
    for d in s_D_list:
        if c + d <= max_F:
            s_list.append(c + d)
s_list = list(set(s_list))  # 3000以下

max_d = -float('inf')
for w in w_list:
    for s in s_list:
        limit_s = w * limit_E / 100
        if w + s <= max_F and w + s != 0 and s <= limit_s:
            d = (s / (w + s)) * 100
            if d > max_d:
                max_d = d
                ans_ws, ans_s = w + s, s

ans = ' '.join([str(ans_ws), str(ans_s)])
print(ans)
