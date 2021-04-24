#!/usr/bin/env python3

N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))

cumsum_list = []
for i, a in enumerate(a_list):
    if i == 0:
        cumsum_list.append(a)
    else:
        cumsum_list.append(cumsum_list[i-1] + a)
    if i < K -1:
        continue
    elif i == K - 1:
        ans = cumsum_list[i]
        print(ans)
    else:
        ans = cumsum_list[i] - cumsum_list[i-K]
        print(ans)

# print(cumsum_list)