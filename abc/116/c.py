# https://atcoder.jp/contests/abc116/tasks/abc116_c
# C - Grand Garden
import copy

n = int(input().split()[0])
h_list = list(map(int, input().split()))

now_h_list = [0] * n
nokori_h_list = copy.copy(h_list)
# 連続するコマの最小値分だけOK
# 最初の1回は、0以外全部いける
count = 0

for i in range(n):

    while nokori_h_list[i] > 0:
        zero_index = nokori_h_list[i:].index(0) if 0 in nokori_h_list[i:] else - 1
        zero_index += i
        if zero_index < i:
            h_add = min(nokori_h_list[i:])
            count += h_add
            nokori_h_list[i:] = map(lambda x: x - h_add, nokori_h_list[i:])
        else:
            h_add = min(nokori_h_list[i:zero_index])
            count += h_add
            nokori_h_list[i:zero_index] = map(lambda x: x - h_add, nokori_h_list[i:zero_index])
        # print(nokori_h_list)

print(count)