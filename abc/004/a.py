# https://atcoder.jp/contests/arc004/tasks/arc004_1
# A - 2点間距離の最大値 ( The longest distance )

import math

n = int(input().split()[0])

point_list = []

for _ in range(n):
	x, y = list(map(int, input().split()))
	point_list.append(dict(x=x, y=y))

def calc_length(a: dict, b: dict):
	return (a['x'] - b['x'])**2 + (a['y'] - b['y'])**2

length_list = []

for i, a in enumerate(point_list):
	for b in point_list[i+1:]:
		length_list.append(calc_length(a, b))

answer = math.sqrt(max(length_list))
print(str(answer) + '\n')
