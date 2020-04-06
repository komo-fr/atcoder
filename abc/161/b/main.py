#!/usr/bin/env python3

N, M = list(map(int, input().split()))
a_list = list(map(int, input().split()))
total = sum(a_list)
b_list = [a for a in a_list if a >= total * (1 / (4 * M))]
ans = "Yes" if len(b_list) >= M else "No"

print(ans)
