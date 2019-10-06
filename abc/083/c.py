# https://atcoder.jp/contests/abc083/tasks/arc088_a
# C - Multiple Gift
import math

x, y = list(map(int, input().split()))

# 一番小さい数でyが限界になるまで倍々していけばよい？
target_list = [x]
number = x

while number * 2 <= y:
    target_list.append(number * 2)
    number = number * 2

# print(target_list)
ans = len(target_list)
print(ans)
