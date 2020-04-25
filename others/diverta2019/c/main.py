#!/usr/bin/env python3

N = int(input().split()[0])
s_list = []
a_list = []
b_list = []
ab_list = []
ab_count = 0
for _ in range(N):
    s = input()
    s_list.append(s)
    ab_count += s.count("AB")
    if s[0] == "B" and s[-1] == "A":
        ab_list.append(s)
    elif s[0] == "B":
        b_list.append(s)
    elif s[-1] == "A":
        a_list.append(s)

if a_list:
    if ab_list:
        a_list.pop()
        ab_count += len(ab_list)
        if b_list:
            ab_count += 1
            b_list.pop()
        ab_count += max(min(len(a_list), len(b_list)), 0)
    else:
        ab_count += min(len(a_list), len(b_list))
elif b_list:
    ab_count += len(ab_list)
else:
    ab_count += max(len(ab_list) - 1, 0)

ans = ab_count
print(ans)
