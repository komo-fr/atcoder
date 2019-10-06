# https://atcoder.jp/contests/abc051/tasks/abc051_b
# Sum of Three Integers

k, s = list(map(int, input().split()))

count = 0

for x in range(k+1):
	for y in range(k+1):
		z = s - (x + y)
		if 0 <= z <= k:
			count += 1

print(count)
