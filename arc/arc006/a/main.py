#!/usr/bin/env python3

e_list = list(map(int, input().split()))
b = int(input().split()[0])
l_list = list(map(int, input().split()))
c = 0
for e in e_list:
    if e in l_list:
        c += 1

if c == 6:
    ans = 1
elif c == 5:
    ans = 2 if b in l_list else 3
elif c < 3:
    ans = 0
else:
    ans = 4 if c == 4 else 5

print(ans)
