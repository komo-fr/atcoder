# https://atcoder.jp/contests/abc043/tasks/arc059_a
# C - いっしょ / Be Together
import statistics
N = int(input().split()[0])
a_list = list(map(int, input().split()))

# たかだか200なので、全探索で間に合う
min_cost = float('inf')

for x in range(-100, 101):
    cost = 0
    for a in a_list:
        cost += (a - x) ** 2
    if cost < min_cost:
        min_cost = cost

print(min_cost)
