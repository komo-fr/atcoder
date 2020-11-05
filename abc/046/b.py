# https://atcoder.jp/contests/abc046/tasks/abc046_b
# Painting Balls with AtCoDeer
input_list = list(map(int, input().split()))
n, k = input_list[0], input_list[1]

p = k
for _ in range(n-1):
    p *= k - 1

print(p)