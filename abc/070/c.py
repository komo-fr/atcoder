# https://atcoder.jp/contests/abc070/tasks/abc070_c
# C - Multiple Clocks
import fractions

n = int(input().split()[0])
t_list = []

for _ in range(n):
    t_list.append(int(input().split()[0]))

t_list = list(set(t_list))
a = t_list[0]

for t in t_list[1:]:
    a = a * t // fractions.gcd(a, t)

print(a)
