#!/usr/bin/env python3

N = int(input().split()[0])
a, b = list(map(int, input().split()))
K = int(input().split()[0])
p_list = list(map(int, input().split()))

if a in p_list or b in p_list or len(set(p_list)) != len(p_list):
    ans = "NO"
else:
    ans = "YES"
print(ans)
