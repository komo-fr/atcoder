# https://atcoder.jp/contests/abc086/tasks/arc089_a

n = int(input().split()[0])

txy_list = []

for i in range(0, n):
    work_list = list(map(int, input().split()))
    txy_list.append(work_list)

pre_txy = [0, 0, 0]
answer = False

for txy in txy_list:
    t, x, y = txy[0], txy[1], txy[2]
    pre_t, pre_x, pre_y = pre_txy[0], pre_txy[1], pre_txy[2]

    t_w, x_w, y_w = t - pre_t, abs(x - pre_x), abs(y - pre_y)
    work = t_w - (x_w + y_w)

    if (work % 2 == 0) and (work >= 0):
        pre_txy = txy
        continue
    else:
        break
else:
    answer = True

a = 'Yes' if answer else 'No'
print(a)