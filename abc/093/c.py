# https://atcoder.jp/contests/abc093/tasks/arc094_a
# C - Same Integers

a, b, c = list(map(int, input().split()))

abc_list = sorted([a, b, c])
c = 0

if (abc_list[1] - abc_list[0]) % 2 != 0:
    # 2番目と3番目に+1することで、最小値と2番目の差を偶数にする
    c += 1
    abc_list[1] += 1
    abc_list[2] += 1

# 最小値と2番目の値を揃える
c += (abc_list[1] - abc_list[0]) / 2
abc_list[0] += 2 * ((abc_list[1] - abc_list[0]) / 2)

# 両方をmax値まで揃える
c += (abc_list[2] - abc_list[1])
c = int(c)

print(c)
