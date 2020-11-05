# https://atcoder.jp/contests/abc079/tasks/abc079_c
# C - Train Ticket

a, b, c, d = list(input().split()[0])
a, b, c, d = [int(x) for x in [a, b, c, d]]

# 2 ** 3通りなので全探索でいけそう
is_ok = False

for op1 in [True, False]:
    work_1 = a + b if op1 else a - b
    for op2 in [True, False]:
        work_2 = work_1 + c if op2 else work_1 - c
        for op3 in [True, False]:
            work_3 = work_2 + d if op3 else work_2 - d
            if work_3 == 7:
                is_ok = True
                op_list = [op1, op2, op3]
                break
        if is_ok:
            break
    if is_ok:
        break

op_list = ['+' if op else '-' for op in op_list]
ans = str(a) + op_list[0] + str(b) + op_list[1] + str(c) + op_list[2] + str(d) + '=7'
print(ans)
