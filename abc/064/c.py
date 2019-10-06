# https://atcoder.jp/contests/abc064/tasks/abc064_c
# C - Colorful Leaderboard

n = int(input().split()[0])
a_list = list(map(int, input().split()))

start, end = 0, 399
rate_dict = {}
rate_id = 0

while end < 3200:
    # 灰色が1-399ではなく0-399になるが
    # 影響はないので0-で実装
    data = dict(start=start, end=end)
    rate_dict[rate_id] = data
    rate_id += 1
    start += 400
    end += 400

count_dict = {rate_id: 0 for rate_id in rate_dict.keys()}

for a in a_list:
    for rate_id, v in rate_dict.items():
        if v['start'] <= a <= v['end']:
            count_dict[rate_id] += 1

count_over = n - sum(count_dict.values())
ALL_COLOR_N = len(count_dict.keys())  # 8色

# 0人の色数
zero_color_n = len([v for v in count_dict.values() if v == 0])

# 最小値
if count_over == n:
    # 全員オーバー
    min_n = 1
else:
    # すでに人がいる色に割り振れば良いので、色数は増えない
    min_n = ALL_COLOR_N - zero_color_n

# 最大値
# オーバーの人は、既存の8色以外も選べる
max_n = (ALL_COLOR_N - zero_color_n) + count_over

ans = ' '.join([str(min_n), str(max_n)])
print(ans)
