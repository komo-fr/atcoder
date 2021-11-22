#!/usr/bin/env python3
from collections import defaultdict

N, X = list(map(int, input().split()))
a_list = list(map(int, input().split()))

done_dict = defaultdict(lambda: False)

# 次に噂を広める相手
next_friend = X
count = 0
while not done_dict[next_friend]:
    count += 1
    done_dict[next_friend] = True
    next_friend = a_list[next_friend - 1]

ans = count
print(ans)
