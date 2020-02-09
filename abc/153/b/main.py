#!/usr/bin/env python3

h, n = list(map(int, input().split()))
a_list = list(map(int, input().split()))
ans = "Yes" if sum(a_list) >= h else "No"
print(ans)
