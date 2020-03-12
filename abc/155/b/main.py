#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
e_list = [a for a in a_list if a % 2 == 0]

if not e_list:
    ans = "APPROVED"
else:
    ee_list = [e for e in e_list if e % 3 == 0 or e % 5 == 0]
    ans = "APPROVED" if len(ee_list) == len(e_list) else "DENIED"

print(ans)
