#!/usr/bin/env python3

a_r_list = []
a_c_list = [[],[],[]]
a_table = []
for _ in range(3):
    a_list = list(map(int, input().split()))
    a_r_list.append(a_list)
    for i, a in enumerate(a_list):
        a_c_list[i].append(a)
    a_table.append(a_list)
a_list_list = a_r_list + a_c_list
a_list_list += [[a_table[0][0], a_table[1][1], a_table[2][2]]]
a_list_list += [[a_table[0][2], a_table[1][1], a_table[2][0]]]

N = int(input().split()[0])
is_ok = False
for _ in range(N):
    b = int(input().split()[0])
    for a_list in a_list_list:
        try:
            a_list.remove(b)
        except ValueError:
            pass
        if not a_list:
            is_ok = True
ans = "Yes" if is_ok else "No"
print(ans)
