#!/usr/bin/env python3

S = input()
K = int(input().split()[0])
c = 0
is_change_tail = False

unit_c = 0

# 連続する文字が奇数かどうか
# 先頭と末尾が異なる場合はシンプル
# 先頭と末尾が同じ場合は、
is_seq = False
count_seq_start = 1  # 先頭からの連続文字数
count_seq_end = 1  # 末尾の連続文字数

# 先頭からの連続文字数を数える
for i in range(1, len(S)):
    if S[i] == S[0]:
        count_seq_start += 1
    else:
        break

# 末尾からの連続文字数を数える
count_seq_end = 1  # 末尾の連続文字数

for i in range(1, len(S)):
    if S[-1 - i] == S[-1]:
        count_seq_end += 1
    else:
        break

count_seq = 1
for i in range(1, len(S)):
    if S[i] == S[i - 1]:
        count_seq += 1
    else:
        # count_seqの偶奇判定
        if count_seq % 2 == 0:
            unit_c += count_seq // 2
        else:
            unit_c += (count_seq - 1) // 2
        count_seq = 1

# 末尾まで連続していた時の処理
# 末尾が1文字だけの場合は、unit_cには0が足されるのでOK
# 末尾が2文字以上の場合、まだunit_cにはカウントされていないのでここで足してOK
if count_seq % 2 == 0:
    unit_c += count_seq // 2
else:
    unit_c += (count_seq - 1) // 2

c += unit_c * K

if S[0] == S[-1] and count_seq_start % 2 == 1 and count_seq_end % 2 == 1:
    c += K - 1

ans = c
print(ans)
