n = int(input().split()[0])
p_list = list(map(int, input().split()))

r_count = 0
target_index_dict = {}
for i, number in enumerate(p_list):
    if i+1 != number:
        r_count += 1
        target_index_dict[i] = number

if not target_index_dict:
    ans = 'YES'
else:
    if len(target_index_dict) >= 3:
        ans = 'NO'
    else:
        a_key = list(target_index_dict.keys())[0]
        a_value = target_index_dict[a_key]
        b_key = list(target_index_dict.keys())[1]
        b_value = target_index_dict[b_key]
        if (a_key+1 == b_value) and (b_key+1 == a_value):
            ans = 'YES'

print(ans)
