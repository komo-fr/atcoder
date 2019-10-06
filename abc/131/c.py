# https://atcoder.jp/contests/abc131/tasks/abc131_c
# C - Anti-Division
import fractions

a, b, c, d = list(map(int, input().split()))

c_n = (b // c) - ((a - 1) // c)
d_n = (b // d) - ((a - 1) // d)

lcm = (c * d) // fractions.gcd(c, d)
lcm_n = (b // lcm) - ((a - 1) // lcm)

ans = (b - a + 1) - (c_n + d_n - lcm_n)
print(ans)
