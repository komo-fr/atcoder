# https://atcoder.jp/contests/abc085/tasks/abc085_c

n, y = list(map(int, input().split()))

done = False

for n_manen in range(0, n+1):
    for n_gosen in range(0, n+1):
        n_sen = n - n_manen - n_gosen
        if n_sen < 0:
            continue
        if n != n_manen + n_gosen + n_sen:
            continue
        total = 10000 * n_manen + 5000 * n_gosen + 1000 * n_sen
        if total == y:
            done = True
            break
    if done:
        break
else:
    n_manen, n_gosen, n_sen = -1, -1, -1

print('{} {} {}'.format(n_manen, n_gosen, n_sen))
