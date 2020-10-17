# https://atcoder.jp/contests/abc078/tasks/arc085_a
# C - HSI

N, M = list(map(int, input().split()))
exp_v = 0

# 1回で全ケースが通る場合は、
# 1900 * M + 100 * (N - M)
# 必ず1回は提出する必要があるので、上記は固定値
# 追加でかかる時間をtと置くと
# 1900 * M + 100 * (N - M) + t
# 一つのケースが通る確率が、p = 1 / 2
# 全てのケースが1回で通る確率が、P = p ** M
# 全ケースが1回で通らない = 追加時間が発生する確率が 1 - P
# 追加でかかる時間を知りたい
# t = (1900 * M + 100 * (N - M)) + (1-P) * t
# C = (1900 * M + 100 * (N - M)) とすると
# t = C + (1-P) * t
# t - C = (1-P) * t
# 1 - C/t = 1 - P
# C / t = P
# t = C / P
# t =  (1900 * M + 100 * (N - M)) / (p ** M)

X = 1900 * M + 100 * (N-M)
t = X / ((1/2) ** M)

print(int(t))
