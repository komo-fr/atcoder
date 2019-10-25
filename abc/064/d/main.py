#!/usr/bin/env python3
import collections

N = int(input().split()[0])
S = input()

# 外側に括弧をつけた方が辞書順は小さい
# ['(((()))())', '((()))()()']

# (の数と)の数は一致すべき
# 最低でも、足りていない方を足りていない分だけ追加することになる
# 一致している場合でも、OKとは限らない
# counter = collections.Counter(S)
# if '(' not in counter.keys() or counter['('] < counter[')']:

# ()
# ))
# ((
# )( がある場合は、そこで一区切りつく
# )(と()があれば、その間の長さで確定する

w_dict = {}
j = 0
before = ""
ext_n_open = 0
ext_n_close = 0
sub_s = ""

for i, ch in enumerate(list(S)):
    if i == 0:
        sub_s += ch
        continue

    if (S[i - 1] == ")" and ch == "(") or i == N - 1:
        # )(だったら
        sub_s += ch
        counter = collections.Counter(sub_s)
        ext_n_open += max(0, counter["("] - counter[")"])
        ext_n_close += max(0, counter[")"] - counter["("])
        sub_s = ""
    else:
        # )), ((, ()
        sub_s += ch

if ext_n_open < ext_n_close:
    ans = "(" * (ext_n_close - ext_n_open) + S
elif ext_n_open > ext_n_close:
    ans = S + ")" * (ext_n_open - ext_n_close)
else:
    ans = "(" * ext_n_open + S + ")" * ext_n_close

print(ans)
