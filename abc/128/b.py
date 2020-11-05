# https://atcoder.jp/contests/abc128/tasks/abc128_b
# B - Guidebook

n = int(input().split()[0])

point_list = []

for i in range(n):
    r, p = list(map(str, input().split()))
    data = dict(index=i+1, city=r, point=int(p))
    point_list.append(data)

sorted_list = sorted(point_list, key=lambda x: (x['city'], -x['point']))

for data in sorted_list:
    print(data['index'])

