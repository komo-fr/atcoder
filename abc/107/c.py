# https://atcoder.jp/contests/abc107/tasks/arc101_a
# C - Candles

n, k = list(map(int, input().split()))
x_list = list(map(int, input().split()))
x_list = sorted(x_list)
min_l = float('inf')

minus_list = [x for x in x_list if x < 0]
plus_index = len(minus_list)

for i, x in enumerate(x_list):
    left, right = x_list[i], x_list[i+k-1]
    # 最左端に行ってから、最右端に行く
    a = abs(left) + abs(left-right)
    # 最右端に行ってから、最左端に行く
    b = abs(right) + abs(right - left)
    l = min(a, b)

    if l < min_l:
        min_l = l

    if i + k > n - 1:
        break

print(min_l)
