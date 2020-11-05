# https://atcoder.jp/contests/abc088/tasks/abc088_b
n = input().split()[0]
a_list = list(map(int, input().split()))

alice_list = []
bob_list = []
sorted(a_list)

for i in range(len(a_list)):
    max_a = max(a_list)
    a_list.remove(max_a)

    if i % 2 == 0:
        alice_list.append(max_a)
    else:
        bob_list.append(max_a)

answer = sum(alice_list) - sum(bob_list)
print(answer)