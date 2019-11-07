#!/usr/bin/env python3
import fractions

N, M = list(map(int, input().split()))
S = input()
T = input()

# 最小公倍数を求める
if N == M:
    l = -1
    if S == T:
        l = N
else:
    if N > M:
        w_n, w_m = N, M
        w_s, w_t = S, T
    else:
        w_n, w_m = M, N
        w_s, w_t = T, S

    if w_n % w_m == 0:
        k = w_n // w_m
        is_ok = True
        l = len(w_s)
        for i, char in enumerate(w_t):
            if S[(i - 1) ** k] != char:
                is_ok = False
                break
        if not is_ok:
            l = -1
    else:
        # 最小公倍数が候補
        l = w_m * w_n // fractions.gcd(w_m, w_n)
        is_ok = True
        s_idx_list = []
        t_idx_list = []

        # w_mの方が小さいのでw_mを基準にする
        for i in range(w_n):
            s_idx_list.append(i * (l // w_n))
            t_idx_list.append(i * (l // w_m))
        common_idx_list = list(set(s_idx_list) & set(t_idx_list))

        for j in common_idx_list:
            s_idx = w_n * j // l
            t_idx = w_m * j // l
            if t_idx > w_m - 1:
                break
            if w_s[s_idx] != w_t[t_idx]:
                is_ok = False
                break
        if not is_ok:
            l = -1

ans = l

print(ans)
