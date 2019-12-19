#!/usr/bin/env python3

s = input()
before = ""
count = 1
pswd = ""
for i, ch in enumerate(s):
    if i == 0:
        before = ch
        continue
    if ch == s[i - 1]:
        count += 1
    else:
        pswd += before + str(count)
        before = ch
        count = 1

pswd += before + str(count)
ans = pswd
print(ans)
