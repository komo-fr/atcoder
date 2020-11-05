# https://atcoder.jp/contests/abc051/tasks/abc051_c
# C - Back and Forth

sx, sy, tx, ty = list(map(int, input().split()))

done_list = []
route_list = []

# 1回目
route_list += ['R'] * abs(sx - tx)
route_list += ['U'] * abs(sy - ty)
route_list += ['L'] * abs(sx - tx)
route_list += ['D'] * abs(sy - ty)

# 2回目（ひとつ大回り）
route_list += ['L']
route_list += ['U'] * (abs(sy - ty) + 1)
route_list += ['R'] * (abs(sx - tx) + 1)
route_list += ['D']
route_list += ['R']
route_list += ['D'] * (abs(sy - ty) + 1)
route_list += ['L'] * (abs(sx - tx) + 1)
route_list += ['U']

ans = ''.join(route_list)
print(ans)
