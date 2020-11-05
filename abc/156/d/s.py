import math

n, a, b = list(map(int, input().split()))


def C(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


mod = 10 ** 9 + 7

t = 0
t_2 = 0
m = 0
for i in range(1, n + 1):
    m += math.factorial(n)
    tmp = C(n, i)
    t += tmp
    if i in [a, b]:
        continue
    t_2 += tmp
print(t)
print(t_2)
print("-----------")

print(t_2 % mod)
print(m)
