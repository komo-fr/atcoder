# https://atcoder.jp/contests/abc049/tasks/arc065_a
s = input().split()[0]
word_list = ['dream', 'dreamer', 'erase', 'eraser']

# erasedream
work_s = s
kumiawase = []

def check_end(text: str, k_word_list):
    ok_word = []
    for word in k_word_list:
        if text.endswith(word):
            ok_word.append(word)
    return ok_word

answer = 'NO'

while work_s:
    ok_word = check_end(work_s, word_list)
    if not ok_word:
        break

    # 後ろから見た場合かぶらないので、これは1回しか動かないはず
    for next_word in ok_word:
        work_s = work_s[:-len(next_word)]
else:
    answer = 'YES'

print(answer)
