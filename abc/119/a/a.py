#!/usr/bin/env python
S = input().split()[0]
s = ''.join(S.split('/'))

if int(s) <= 20190430:
    ans = 'Heisei'
else:
    ans = 'TBD'

print(ans)
