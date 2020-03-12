#!/usr/bin/env python3

N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))

m_list = []
z_list = []
p_list = []

m, z, p = 0, 0, 0
m_absmax = float("inf")

for a in a_list:
    if a < 0:
        m_list.append(a)
        m += 1
    elif a == 0:
        z_list.append(a)
        z += 1
    else:
        p_list.append(a)
        p += 1

m_list = list(sorted(m_list))
p_list = list(sorted(p_list))

# マイナスの数
m_c = m * p
# ゼロの数
z_c = z * (m + p) + (z * (z - 1)) / 2
# プラスの数
p_c = (p * (p - 1) / 2) + (m * (m - 1) / 2)

print("------")
print(m_c + z_c + p_c == (N * (N - 1)) / 2)
print("------")


if K <= m_c:
    m_list = list(sorted(m_list, reverse=True))
    p_list = list(sorted(p_list, reverse=True))
elif K <= m_c + z_c:
    ans = 0
else:
    m_list = list(sorted(m_list))
    p_list = list(sorted(p_list))

print(ans)
