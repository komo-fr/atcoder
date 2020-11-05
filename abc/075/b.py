# https://atcoder.jp/contests/abc075/tasks/abc075_b
hw_list = list(map(int, input().split()))
h_max = hw_list[0]
w_max = hw_list[1]

s_list = []

for i in range(h_max):
    work_list = input()
    s_list.append(work_list)
answer_list = []

for h in range(h_max):
    work_list = s_list[h]
    work_answer = []
    for w, target in enumerate(work_list):
        if target == '.':
            tonari_list = [(w-1, h-1), (w, h-1), (w+1, h-1),
                           (w-1, h), (w+1, h),
                           (w-1, h+1), (w, h+1), (w+1, h+1)]
            count = 0
            for x, y in tonari_list:
                if 0 <= x < w_max and 0 <= y < h_max:
                    if s_list[y][x] == '#':
                        count += 1
                else:
                    continue
            work_answer.append(str(count))
        else:
            work_answer.append('#')
    answer_list.append(work_answer)

for a_list in answer_list:
    print(''.join(a_list))
