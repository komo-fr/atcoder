# https://atcoder.jp/contests/abc130/tasks/abc130_c
# C - Rectangle Cutting

w, h, x, y = list(map(int, input().split()))

center_x = w / 2
center_y = h / 2

if center_x == x and center_y == y:
    ans_b = 1
else:
    ans_b = 0

ans_a = w * h / 2

print('{} {}'.format(ans_a, ans_b))
