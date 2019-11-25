#!/usr/bin/env python3

S = input()
a_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
# a_list = list(reversed(a_list))
c = 0
for a in a_list:
    c += 1
    if S == a:
        ans = 7 - c + 1

print(ans)
