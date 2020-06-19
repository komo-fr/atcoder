#!/usr/bin/env python3

a_list = list(map(int, input().split()))
ans = sorted(a_list)[-3]
print(ans)
