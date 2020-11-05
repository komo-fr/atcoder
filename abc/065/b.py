# https://atcoder.jp/contests/abc065/tasks/abc065_b
# B - Trained?
n = int(input().split()[0])

index2number_dict = {}
number2index_dict = {}
button_list = []

for _ in range(n):
    number = int(input().split()[0])
    button_list.append(number)
    

# ボタンが光っているときに押すと、
# 今のボタンの光が消える
# 次のボタンが光る
# ボタン2が光っている状態でやめたい
# print(index2number_dict)

start_index = 1
# print(start_number)
# print(start_index)

step = 0
lighting_index = start_index # 1 - n
status_list = ''
can_stop = False

while True:
    status_list += str(lighting_index)

    lighting_number = button_list[lighting_index - 1]
    lighting_index = lighting_number  # 次のインデックス
    step += 1


    if lighting_index == 2:
        can_stop = True
        break

    if step >= len(button_list):
        break
    # print('i = {}, ai = {}'.format(lighting_index, lighting_number))
    

    # print('Next -> i = {}, a_i = {} '.format(lighting_index, lighting_number))
    

if not can_stop:
    step = -1

# print('===========')
# print(status_list)
print(step)