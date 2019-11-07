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
        for i in range(l):
            s_idx = i * (l // w_n)
            t_idx = i * (l // w_m)
            if t_idx > w_m - 1:
                break
            if s_idx != t_idx:
                continue
            if w_s[s_idx] != w_t[t_idx]:
                is_ok = False
                break
        if not is_ok:
            l = -1

ans = l

print(ans)
