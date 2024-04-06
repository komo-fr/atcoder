#!/usr/bin/env python3

a_list = list(map(int, input().split()))
ans = "Yes" if len(set(a_list)) == 1 else "No"
print(ans)
