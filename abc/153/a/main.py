#!/usr/bin/env python3

h, a = list(map(int, input().split()))
c = h // a if h % a == 0 else h // a + 1

ans = c
print(ans)
