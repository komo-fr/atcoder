# B - Two Switches
# https://atcoder.jp/contests/abc070/tasks/abc070_b
# 11分、AC1回

a_list = list(map(int, input().split()))
a, b, c, d = a_list[0], a_list[1], a_list[2], a_list[3]

start = 0
alice_time = (a, b)
bob_time = (c, d)

max_end = max(b, d)
alice_zone = [0] * max_end
bob_zone = [0] * max_end
alice_zone[a:b] = [1] * len(alice_zone[a:b])
bob_zone[c:d] = [1] * len(bob_zone[c:d])

kasanari_zone = [alice * bob for alice, bob, in zip(alice_zone, bob_zone)]
print(sum(kasanari_zone))
