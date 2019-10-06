# https://atcoder.jp/contests/abc002/tasks/abc002_3
# C - 直訴

a_x, a_y, b_x, b_y, c_x, c_y = list(map(int, input().split()))

new_b = (b_x-a_x, b_y-a_y)
new_c = (c_x-a_x, c_y-a_y)

ans = abs(new_b[0] * new_c[1] - new_b[1] * new_c[0]) / 2
print(ans)
