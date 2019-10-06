# https://atcoder.jp/contests/abc077/tasks/arc084_a
# C - Snuke Festival
import bisect

N = int(input().split()[0])
a_list = sorted(list(map(int, input().split())))
b_list = sorted(list(map(int, input().split())))
c_list = sorted(list(map(int, input().split())))

comb_n = 0
comb_n_list = []

# 自分より大きい個数
start_c_index = 0
start_a_index = 0

for i in range(N):  # 10 ** 5
    b = b_list[i]
    a_n = bisect.bisect_left(a_list, b)
    c_n = N - bisect.bisect_right(c_list, b)
    comb_n += a_n * c_n
ans = comb_n
print(ans)
