# https://atcoder.jp/contests/abc100/tasks/abc100_c
# C - *3 or /2
import math

n = int(input().split()[0])
a_list = list(map(int, input().split()))

# 2で割れる数は何回か
def f(value):
    x = value
    count = 0
    while x % 2 == 0:
        x = x / 2
        count += 1
    return count

ans = sum([f(a) for a in a_list])
print(int(ans))
