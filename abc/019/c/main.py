#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))

group_dict = {}
group_id = 0


# 奇数 x (2 ** n)の形に落とせる
# 奇数の種類の数が、答えとなる
def divide_two(source):
    n, a = divmod(source, 2)
    if a != 0:
        return source
    else:
        before = n
        while a == 0:
            before = n
            n, a = divmod(n, 2)
        n = before
    return n


odd_list = []

for a in a_list:
    odd_list.append(divide_two(a))

ans = len(list(set(odd_list)))

print(ans)
