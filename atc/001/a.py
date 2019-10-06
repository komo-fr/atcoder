# https://atcoder.jp/contests/atc001/tasks/dfs_a
# A - 深さ優先探索

import sys
sys.setrecursionlimit(1000000)

h, w = list(map(int, input().split()))
c_map_list = []

for _ in range(h):
    c = list(input().split())[0]
    c = [x for x in c]
    c_map_list.append(c)

filled_map_list = [[''] * w for _ in range(h)]

start_x, start_y = None, None

for i, c_list in enumerate(c_map_list):
    if 's' not in c_list:
        continue

    start_x = c_list.index('s')
    start_y = i

# print('x={}, y={}'.format(start_x, start_y))

goal_flag = False

def print_filled_map(input_list):
    print('-----------')
    for row in input_list:
        print(row)


def search(now_x, now_y):
    # print_filled_map(filled_map_list)

    if now_x < 0 or w <= now_x or now_y < 0 or h <= now_y:
        # 行き止まり ここにはいけない
        return

    if c_map_list[now_y][now_x] == '#':
        # ここは壁
        return

    if filled_map_list[now_y][now_x] == 'x':
        # ここは探索済
        return

    # ここは探索済
    filled_map_list[now_y][now_x] = 'x'
    global goal_flag
    if c_map_list[now_y][now_x] == 'g':
        goal_flag = True
        return

    search(now_x-1, now_y)
    search(now_x+1, now_y)
    search(now_x, now_y-1)
    search(now_x, now_y+1)


search(start_x, start_y)

answer = 'Yes' if goal_flag else 'No'

print(answer)
