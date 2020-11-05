# https://atcoder.jp/contests/abc121/tasks/abc121_c
# C - Energy Drink Collector

n, m = list(map(int, input().split()))
ab_list = []

for _ in range(n):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))

# 一番安いお店を探す
ab_list.sort(key=lambda val: val[0])
nokori = m
cost = 0

for a, b in ab_list:
    if nokori < b:
        cost += a * nokori
        break
    else:
        cost += a * b
        nokori -= b

print(cost)
