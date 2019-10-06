
# https://atcoder.jp/contests/abc097/tasks/arc097_a
# C - K-th Substring

s = input().split()[0]
K = int(input().split()[0])

sub_s_list = []
N = len(s)
sorted_char_list = sorted(list(set(s)))
char_N = len(sorted_char_list)

# Kは最大で5であることに着目する
# 全部列挙する必要はなく、5番目まで見つかればよい
# 最初の1文字目
start_index_list = [i for i, char in enumerate(s) if char == sorted_char_list[0]]
pattern = sorted_char_list[0]
sorted_char_list.remove(pattern)
char_i = 0
j = 1

waiting_list = []

while len(sub_s_list) < 5:
    # print(pattern)
    sub_s_len = len(pattern)
    sub_s_list.append(pattern)
    next_list = [s[i:i+sub_s_len+1]
                for i in start_index_list
                if (i <= N - (sub_s_len + 1)) and (s[i:i+sub_s_len] == pattern)]

    if not next_list:
        if min(start_index_list) + sub_s_len > N:
            # 末尾まで伸びた
            if waiting_list:
                pattern = waiting_list[0]
                waiting_list.remove(pattern)
            elif sorted_char_list:
                pattern = sorted_char_list[0]
                start_index_list = [i for i, char in enumerate(s) if char == sorted_char_list[0]]
                sorted_char_list.remove(pattern)
        else:
            # 末尾まで伸ばす
            next_waiting_list =  [s[i:i+sub_s_len+1] for i in start_index_list
                                    if (i <= N - (sub_s_len + 1))]
            # print(next_waiting_list)
            waiting_list += next_waiting_list
            waiting_list = list(set(waiting_list))

            if waiting_list:
                waiting_list = sorted(waiting_list)
                pattern = waiting_list[0]
                waiting_list.remove(pattern)
            elif sorted_char_list:
                pattern = sorted_char_list[0]
                start_index_list = [i for i, char in enumerate(s) if char == sorted_char_list[0]]
                sorted_char_list.remove(pattern)
    else:
        waiting_list += next_list
        waiting_list = sorted(list(set(waiting_list)))
        pattern = waiting_list[0]
        waiting_list.remove(pattern)
    # print(waiting_list)

sub_s_list = list(set(sub_s_list))
ans = sorted(sub_s_list)[K-1]
print(ans)
