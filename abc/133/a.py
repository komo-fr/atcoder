# https://atcoder.jp/contests/abc133/tasks/abc133_a
# A - T or T

n, a, b = list(map(int, input().split()))

train = a * n
taxi = b

ans = min([train, taxi])
print(ans)