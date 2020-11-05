# https://atcoder.jp/contests/abc106/tasks/abc106_c
# C - To Infinity
import re

s = input().split()[0]
k = int(input().split()[0])

m = re.search(r'[2-9]+', s)

if m:
    index = m.start()
    ans = m.group()[0] if index < k else '1'
else:
    ans = '1'

print(ans)
