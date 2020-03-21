h, w = list(map(int, input().split()))
a_table = []

for _ in range(h):
    a_list = list(map(int, input().split()))
    a_table.append(a_list)


a_table = list(zip(*a_table))
is_ok = True

expected_list = list(a_table[0])

for a_list in a_table[1:]:
    is_clear = False
    t_list = list(a_list)
    for i in range(h + 1):
        if t_list == expected_list:
            is_clear = True
            break
        t_list = [t_list[-1]] + t_list[:-1]

    if not is_clear:
        is_ok = False
        break

ans = "Yes" if is_ok else "No"
print(ans)
