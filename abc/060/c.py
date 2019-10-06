# https://atcoder.jp/contests/abc060/tasks/arc073_a
# C - Sentou

N, T = list(map(int, input().split()))
t_list = list(map(int, input().split()))
total = 0

for i in range(1, N):
    diff = t_list[i] - t_list[i-1]
    if diff < T:
        total += diff
    else:
        total += T
total += T

print(total)
