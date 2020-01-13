#!/usr/bin/env python3
import string

s_list = string.ascii_lowercase
c = input()

ans = s_list[s_list.index(c) + 1]
print(ans)
