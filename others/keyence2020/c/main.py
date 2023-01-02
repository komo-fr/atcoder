#!/usr/bin/env python3

N, K, S = list(map(int, input().split()))
if S < 10 ** 9:
    ans_list = [S] * K + [S + 1] * (N - K)
else:
    ans_list = [S] * K + [S - 1] * (N - K)

ans = " ".join([str(x) for x in ans_list])
print(ans)
