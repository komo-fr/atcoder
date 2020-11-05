# https://atcoder.jp/contests/abc035/tasks/abc035_c
# C - オセロ

N, Q = list(map(int, input().split()))
lr_list = []
for _ in range(Q):
    l, r = list(map(int, input().split()))
    lr_list.append((l, r))

imos_list = [0] * N

for lr in lr_list:  # 最悪で2 * 10 ** 6
    l, r = lr
    imos_list[l-1] = imos_list[l-1] + 1
    if r != N:
        imos_list[r] = imos_list[r] - 1

# 累積和を求める
cumsum_list = [0] * N
cumsum_list[0] = imos_list[0]

for i in range(1, N):
    cumsum_list[i] = cumsum_list[i-1] + imos_list[i]

ans_list = ['0' if x % 2 == 0 else '1' for x in cumsum_list]
ans = ''.join(ans_list)
print(ans)
