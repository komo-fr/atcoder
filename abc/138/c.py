n = int(input().split()[0])
v_list = list(map(int, input().split()))

r_v_list = sorted(v_list)

total = 0

for i, v in enumerate(r_v_list[1:]):
    if i == 0:
        total = (r_v_list[0] + v) / 2
    else:
        total = (total + v) / 2

print(total)
