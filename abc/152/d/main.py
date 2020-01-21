#!/usr/bin/env python3
import itertools

N = int(input().split()[0])
s = str(N)
l = list(range(1, 10))
p_gen = itertools.product(l, repeat=2)
p_list = list(p_gen)
K = len(str(s))


def count_kouho(x, y):
    count = 0
    for k in range(1, K + 1):
        # 1桁目
        if k == 1:
            if x == y:
                if x <= N:
                    count += 1
            continue
        # 2桁目
        if k == 2:
            if int(str(x) + str(y)) <= N:
                count += 1
            continue
        # 3桁目以上
        if k == K:
            # 一番大きい桁の場合
            # TODO
            if x < int(s[0]):
                count += 10 ** (k - 2)
            elif x > int(s[0]):
                pass
            else:
                if y <= int(s[-1]):
                    count += int(s[1:-1]) + 1
                else:
                    count += int(s[1:-1])
            continue
        count += 10 ** (k - 2)
    return count


c = 0

for p in p_list:
    head, tail = p
    kouho_1 = count_kouho(head, tail)
    if head == tail:
        kouho_2 = kouho_1
    else:
        kouho_2 = count_kouho(tail, head)
    if kouho_1 < 1 or kouho_2 < 1:
        # print("{} skip".format((head, tail)))
        continue
    new_c = kouho_1 * kouho_2
    # print("{}: {} ({})".format((head, tail), (kouho_1, kouho_2), new_c))
    c += new_c

ans = c
print(ans)
