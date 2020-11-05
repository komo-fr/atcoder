# https://atcoder.jp/contests/abc120/tasks/abc120_a
# A - Favorite Sound

a, b, c = list(map(int, input().split()))

ans = min(b // a, c)
print(ans)