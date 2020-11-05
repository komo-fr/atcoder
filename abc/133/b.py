# https://atcoder.jp/contests/abc133/tasks/abc133_b
# B - Good Distance
import itertools
import math

n, d = list(map(int, input().split()))
x_list = []

for _ in range(n):
    x_list.append(list(map(int, input().split())))

# 全探索でいける？
l = list(range(0, n))
c = itertools.combinations(l, 2)
integer_count = 0

for v in c:
    a_index = v[0]
    b_index = v[1]
    work_list = []
    for a, b in zip(x_list[a_index], x_list[b_index]):
        work_list.append((a - b) ** 2)
    length = math.sqrt(sum(work_list))

    if length.is_integer():
        integer_count += 1

print(integer_count)

