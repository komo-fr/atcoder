# https://atcoder.jp/contests/abc046/tasks/arc062_a
# C - AtCoDeerくんと選挙速報 / AtCoDeer and Election Report

N = int(input().split()[0])
ta_list = []

for _ in range(N):
    t, a = list(map(int, input().split()))
    ta_list.append((t, a))

# 最初のやつ
t, a = ta_list[0]
total_p = t + a
now_t, now_a = t, a

for t, a in ta_list[1:]:
    w_t, w_a = t, a

    c = max(now_t // w_t, now_a // w_a)
    w_t *= c
    w_a *= c

    while w_t < now_t or w_a < now_a:
        w_t += t
        w_a += a

    now_t = w_t
    now_a = w_a
    total_p = now_t + now_a

print(total_p)
