#!/usr/bin/env python3

a_list = list(map(int, input().split()))

ans = list(sorted(a_list))[1]
print(ans)
