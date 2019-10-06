#!/usr/bin/env python3

N = int(input().split()[0])

s = 0
for i in range(1, 10):
    for j in range(1, 10):
        s += i * j

diff = s - N
kouho_list = []

for i in range(1, 10):
    div, mod = divmod(diff, i)
    if mod == 0 and div <= 9:
        kouho_list.append((i, div))

kouho_list = ['{} x {}'.format(a, b) for a, b in kouho_list]
ans = '\n'.join(kouho_list)

print(ans)
