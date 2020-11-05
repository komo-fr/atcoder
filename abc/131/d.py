# https://atcoder.jp/contests/abc131/tasks/abc131_d
# D - Megalomania

n = int(input().split()[0])
ab_list = []
is_ok = True

for _ in range(n):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))

ab_list = sorted(ab_list, key=lambda x: x[1])
now_t = 0
is_ok = True

for i, ab in enumerate(ab_list):
    a, b = ab
    s_deadline = b - a

    if now_t > s_deadline:
        # 現在時刻が、開始時刻のデッドラインを過ぎている
        is_ok = False
        break
    now_t += a

ans = 'Yes' if is_ok else 'No'
print(ans)
