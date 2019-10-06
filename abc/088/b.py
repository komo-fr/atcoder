# https://atcoder.jp/contests/abc088/tasks/abc088_b
# B - Card Game for Two

n = int(input().split()[0])
a_list = list(map(int, input().split()))

a_list = sorted(a_list, reverse=True)
p_alice = sum(a_list[::2])
p_bob = sum(a_list[1::2])
ans = p_alice - p_bob
print(ans)
