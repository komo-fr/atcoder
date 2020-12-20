#!/usr/bin/env python3
from collections import defaultdict

N, Q = list(map(int, input().split()))
c_list = list(map(int, input().split()))
q_list = []


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, i):
        if self.parents[i] == i:
            # 自分自身だったらそのまま返す
            return i
        else:
            # 自分の祖先を、自分の祖先の祖先で更新する
            # こうすることで、途中を飛ばすことができる
            self.parents[i] = self.find(self.parents[i])
            return self.parents[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i != j:
            # print("別の家族なので養子に迎える")
            i, j = min(i, j), max(i, j)

            # 別の家族だったら養子に迎える
            self.parents[j] = i


uf = UnionFind(N)
com2counter = defaultdict(lambda: defaultdict(lambda: 0))
# student2com = {idx: idx for idx in range(N)}
student2com = defaultdict(lambda: None)
com_id = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    # print(f"{q=}")
    # print(f"{uf.parents}")
    if q[0] == 1:
        # 合流
        x_idx = q[1] - 1
        y_idx = q[2] - 1
        uf.union(x_idx, y_idx)
        # クラスの人数を統合する
        class_1 = c_list[x_idx]
        class_2 = c_list[y_idx]
        if student2com[x_idx] is None and student2com[y_idx] is None:
            # 新しい集団
            # print("新しい集団")
            com_id += 1
            com2counter[com_id]["total"] = 2
            com2counter[com_id][class_1] += 1
            com2counter[com_id][class_2] += 1
            student2com[x_idx] = com_id
            student2com[y_idx] = com_id
        elif student2com[x_idx] is not None and student2com[y_idx] is None:
            com2counter[com_id]["total"] += 1
            com2counter[com_id][class_2] += 1
            student2com[y_idx] = student2com[x_idx]
        elif student2com[x_idx] is None and student2com[y_idx] is not None:
            com2counter[com_id]["total"] += 1
            com2counter[com_id][class_1] += 1
            student2com[x_idx] = student2com[y_idx]
        else:
            com_id_1 = student2com[x_idx]
            com_id_2 = student2com[y_idx]
            if com_id_1 == com_id_2:
                continue
            # 小さい方のコミュニティ
            if com2counter[com_id_1]["total"] <= com2counter[com_id_2]["total"]:
                small_com_id = com_id_1
                big_com_id = com_id_2
                student2com[x_idx] = com_id_2
            else:
                small_com_id = com_id_2
                big_com_id = com_id_1
                student2com[y_idx] = com_id_1
            for k, v in com2counter[small_com_id].items():
                com2counter[big_com_id][k] += com2counter[small_com_id][k]
            com2counter[big_com_id]["total"] += com2counter[small_com_id]["total"]

    else:
        x_idx = q[1] - 1
        y_class = q[2]
        target_com_id = student2com[x_idx]
        student_n = com2counter[target_com_id][y_class]
        print(student_n)
