# https://atcoder.jp/contests/abc030/tasks/abc030_c
# C - 飛行機乗り
import bisect

N, M = list(map(int, input().split()))
X, Y = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
t = 0
c = 0
while True:
    # A -> B
    a_index = bisect.bisect_left(a_list, t)
    if a_index >= len(a_list):
        break
    # 出発時刻で更新
    t = a_list[a_index]
    t += X

    # B -> A
    b_index = bisect.bisect_left(b_list, t)
    if b_index >= len(b_list):
        break
    # 出発時刻で更新
    t = b_list[b_index]
    # 移動時間を加算
    t += Y
    c += 1

print(c)
