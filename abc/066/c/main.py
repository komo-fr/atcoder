# https://atcoder.jp/contests/abc066/tasks/arc077_a
# C - pushpush

n = int(input().split()[0])
a_list = list(map(int, input().split()))

pre_list = a_list[1::2][::-1]
suf_list = a_list[::2]

b = pre_list + suf_list

if n % 2 == 1:
    b = b[::-1]

ans = ' '.join([str(x) for x in b])

print(ans)
