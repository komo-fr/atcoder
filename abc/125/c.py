# https://atcoder.jp/contests/abc125/tasks/abc125_c
# C - GCD on Blackboard
import fractions
import itertools
import collections

n = int(input().split()[0])
a_list = list(map(int, input().split()))
sorted_list = sorted(a_list)
min_a, second_min_a = sorted_list[0], sorted_list[1]

def koyakusu(x):
    i = 1
    koyaku_list = []
    while i * i <= x:
        if x % i == 0:
            koyaku_list.append(i)
            koyaku_list.append(x//i)
        i += 1

    koyaku_list = list(set(koyaku_list))
    return koyaku_list

kouho_list = []
# print('{}: {}'.format(min_a, koyakusu(min_a)))
kouho_list += koyakusu(min_a)

# print('{}: {}'.format(second_min_a, koyakusu(second_min_a)))
kouho_list += koyakusu(second_min_a)
kouho_list = list(set(kouho_list))
# print(kouho_list)
ans_kouho_list = []

for kouho in kouho_list:
    x_list = [x for x in a_list if x % kouho == 0]
    # print('kouho {} ({})'.format(kouho, len(x_list)))
    if len(x_list) >= n-1:
        ans_kouho_list.append(kouho)
# print(ans_kouho_list)
ans = max(ans_kouho_list)

print(ans)
