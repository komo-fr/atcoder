# https://atcoder.jp/contests/abc083/tasks/abc083_a
# A - Libra

a, b, c, d = list(map(int, input().split()))

if a + b > c + d:
    ans = 'Left'
elif a + b == c+ d:
    ans = 'Balanced'
else:
    ans = 'Right'

print(ans)
