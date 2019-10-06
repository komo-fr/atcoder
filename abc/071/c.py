# https://atcoder.jp/contests/abc071/tasks/arc081_a
# C - Make a Rectangle
import collections

N = int(input().split()[0])
a_list = list(map(int, input().split()))

counter = collections.Counter(a_list)
count_dict = {k: v for k, v in counter.items() if v >= 2}
if count_dict:
    length_list = sorted(list(count_dict.keys()), reverse=True)

    if len(length_list) == 1 and counter[length_list[0]] < 4:
        area = 0
    elif counter[length_list[0]] >= 4:
        area = length_list[0] ** 2
    else:
        area = length_list[0] * length_list[1]
else:
    area = 0

print(area)
