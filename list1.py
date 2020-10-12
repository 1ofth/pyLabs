from typing import List, Tuple


# 1.
# Вх: список строк, Возвр: кол-во строк
# где строка > 2 символов и первый символ == последнему
def me(words: List[str]) -> int:
    return sum(1 if len(s) > 2 and s[0] == s[-1] else 0 for s in words)


# 2.
# Вх: список строк, Возвр: список со строками (упорядочено)
# за искл всех строк начинающихся с 'x', которые попадают в начало списка.
# ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']
def fx(words: List[str]) -> List[str]:
    words.sort()
    x_list = [x for x in words if len(x) > 0 and x[0] == 'x']
    other_list = [x for x in words if len(x) == 0 or x[0] != 'x']
    return x_list + other_list


# 3.
# Вх: список непустых кортежей,
# Возвр: список сортир по возрастанию последнего элемента в каждом корт.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
def sort_pairs(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return sorted(pairs, key=lambda i: i[-1])
