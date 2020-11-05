n = int(input().split()[0])
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

all_mons_n = sum(a_list)
mons_list = []

for i, b in enumerate(b_list):
    mons_n = a_list[i]
    next_mons_n = a_list[i+1]
    can_hit_n = b

    if mons_n <= can_hit_n:
        a_list[i] = 0
        can_hit_n = can_hit_n - mons_n
    elif mons_n > can_hit_n:
        a_list[i] -= can_hit_n
        can_hit_n = 0

    if can_hit_n > 0:
        if next_mons_n <= can_hit_n:
            a_list[i+1] = 0
            can_hit_n = can_hit_n - next_mons_n
        elif next_mons_n > can_hit_n:
            a_list[i+1] -= can_hit_n

total = all_mons_n - sum(a_list)
print(total)
