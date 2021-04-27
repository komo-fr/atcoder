#!/usr/bin/env python3

N = int(input().split()[0])
ab_list = []
d_list = []
max_aoki = 0

class Mura:
    def __init__(self, index, a, b):
        self.index = index
        self.a = a
        self.b = b
        self.d = a * 2 + b

    def __lt__(self, other):
        return int(self.d) <= int(other.d)
        
for i in range(N):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))
    d_list.append(Mura(i, a, b))
    max_aoki += a

d_list = sorted(d_list, reverse=True)
takahasi_point = 0
aoki_point = max_aoki
count = 0
for mura in d_list:
    count += 1
    takahasi_point += mura.a + mura.b
    aoki_point -= mura.a
    if takahasi_point > aoki_point:
        break

ans = count
print(ans)
