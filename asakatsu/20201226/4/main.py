#!/usr/bin/env python3
from collections import Counter
s = input()
s = s.replace("BC", "D")
count = 0
seq_n = 0
count_a = 0
pre_char = ""
seq = ""
for i, char in enumerate(s):
    if char in ["A", "D"]:
        seq += char
        if char == "A":
            count_a += 1
    else:
        count += Counter(seq[count_a:]))
        seq = ""
        count_a = 0
    
else:
    print(f"{seq_n=}")
    count += seq_n * (seq_n + 1) // 2
    seq_n = 0

ans = count
print(ans)
