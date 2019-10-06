# https://atcoder.jp/contests/abc007/tasks/abc007_3
# C - 幅優先探索
import sys
import itertools

sys.setrecursionlimit(10000000) 
r, c = list(map(int, input().split()))

start_y, start_x = list(map(int, input().split()))
goal_y, goal_x = list(map(int, input().split()))

start_y -= 1
start_x -= 1
goal_y -= 1
goal_x -= 1

c_map_list = []

for _ in range(r):
    c_list = input().split()[0]
    c_map_list.append(c_list)


min_step_map_dict = {}


def show_step():  # for debug
    print('===============')
    for i in range(c):
        show_list = []
        for j in range(r):
            if (j, i) in min_step_map_dict:
                step = str(min_step_map_dict[(j, i)]).zfill(2)
                show_list.append(step)
            else:
                show_list.append('--')
        print(' '.join(show_list))
    print('===============')


def can_go(x, y):
    if x < 0 or x >= c or y < 0 or y >= r:
        # 枠外だったら探索対象外
        return False
    if (x, y) in min_step_map_dict:
        # すでに探索済またはwiting中なので探索対象外
        return False
    if c_map_list[y][x] == '#':
        # 壁だったら探索対象外
        min_step_map_dict[(x, y)] = ' #'
        return False

    return True


def search(now_x, now_y, koremade_step):
    neighbors = [(now_x-1, now_y), # 下
                 (now_x+1, now_y), # 上
                 (now_x, now_y-1), # 左
                 (now_x, now_y+1)] # 右
    next_search_list = []

    for n_x, n_y in neighbors:
        if can_go(n_x, n_y):
            next_search_list.append((n_x, n_y))
            min_step_map_dict[(n_x, n_y)] = koremade_step + 1

    return next_search_list

min_step_map_dict[(start_x, start_y)] = 0
next_search_list = search(start_x, start_y, 0)
step = 1

while True:
    next_search_list_list = []
    for next_target in next_search_list:
        next_x, next_y = next_target[0], next_target[1]
        next_search_list = search(next_x, next_y, step)
        next_search_list_list.append(next_search_list)
    next_search_list = list(itertools.chain.from_iterable(next_search_list_list))
    step += 1
    if not next_search_list:
        break

# show_step() for debug
answer = min_step_map_dict[(goal_x, goal_y)]
print(answer)
