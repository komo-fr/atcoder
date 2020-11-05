# https://atcoder.jp/contests/abc136/tasks/abc136_d
# D - Gathering Children
import math
# 一番近いRLはどこか？

s_list = list(input().split()[0])
count_list = [0] * len(s_list)

# 最初がRだった子は、Rが連続する限り右へ行く。最初にLが出た瞬間が打ち止め
# 最初がLだった子は、Lが連続する限り左へ行く。最初にRが出た瞬間が打ち止め
rrl_list = ''.join(s_list).split('LR')
count_index = 0

for i, rrl in enumerate(rrl_list):
    if i != 0:
        rrl = 'R' + rrl
    if i != len(rrl_list) - 1:
        rrl = rrl + 'L'
    rl_r_index = rrl.find('RL')
    # rl_r_indexから偶数歩離れているマス目の数は
    # 左側
    r_count = math.floor(rl_r_index / 2)
    # print('左側：{}'.format(r_count))
    # 右側
    # print('右側: {}'.format(math.floor((len(rrl) - (rl_r_index+1)) / 2) + 1))
    r_count += math.floor((len(rrl) - (rl_r_index+1)) / 2) + 1

    l_count = len(rrl) - r_count
    count_list[count_index + rl_r_index] = r_count
    count_list[count_index + rl_r_index + 1] = l_count
    count_index += len(rrl)
    # print(rrl)
    # print(count_list)

ans = ' '.join([str(x) for x in count_list])
print(ans)
