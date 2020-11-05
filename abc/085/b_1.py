# https://atcoder.jp/contests/abc085/tasks/abc085_b
# setを使わない解き方
n = int(input().split()[0])
length_list = []

for _ in range(n):
    x = int(input().split()[0])
    length_list.append(x)

length_list = sorted(length_list)
no_dup_list = []

for i in range(len(length_list)):
    if i == len(length_list) - 1:
         no_dup_list.append(x)
    else:
        x = length_list[i]
        next_x = length_list[i + 1]
        if x != next_x:
            no_dup_list.append(x)
        else:
            continue

print(len(no_dup_list))
