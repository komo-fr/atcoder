#!/usr/bin/env python3
import collections

N = int(input().split()[0])
S = input()

ext_n_open, ext_n_close = 0, 0
sub_s = ""

for i, ch in enumerate(list(S)):
    if i == N - 1 or (S[i] == ")" and S[i + 1] == "("):
        # )(だったら
        sub_s += ch
        counter = collections.Counter(sub_s)
        if counter["("] > counter[")"]:
            ext_n_open += counter["("] - counter[")"]
        elif counter["("] < counter[")"]:
            n_close_w = counter[")"] - counter["("]
            n_close = max(0, n_close_w - ext_n_open)
            ext_n_open = max(0, ext_n_open - n_close_w)
            ext_n_close += n_close
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
