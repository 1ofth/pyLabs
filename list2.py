from typing import List


# 1.
# Вх: список чисел, Возвр: список чисел, где
# повторяющиеся числа урезаны до одного
# пример [0, 2, 2, 3] returns [0, 2, 3].

def rm_adj(nums: List) -> List:
    return list(set(nums))


# 2. Вх: Два списка упорядоченных по возрастанию, Возвр: новый отсортированный объединенный список
def merge(a, b: List[int]) -> List[int]:
    ind_a = 0
    ind_b = 0
    merged = []

    while ind_a < len(a) and ind_b < len(b):
        if a[ind_a] < b[ind_b]:
            merged.append(a[ind_a])
            ind_a += 1
        else:
            merged.append(b[ind_b])
            ind_b += 1

    while ind_a < len(a):
        merged.append(a[ind_a])
        ind_a += 1

    while ind_b < len(b):
        merged.append(b[ind_b])
        ind_b += 1

    return merged
