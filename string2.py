# 1. 
# Вх: строка. Если длина > 3, добавить в конец "ing", 
# если в конце нет уже "ing", иначе добавить "ly".
def v(s: str) -> str:
    if len(s) < 4:
        return s
    return s + "ly" if s.endswith("ing") else s + "ing"


# 2.
# Вх: строка. Заменить подстроку от 'not' до 'bad'. ('bad' после 'not')
# на 'good'.
# Пример: So 'This music is not so bad!' -> This music is good!
def replace_not_bad(s: str) -> str:
    left = s.find("not")
    right = s.find("bad")
    if left > 0 and right > 0:
        return s[0:left] + "good" + s[right + 3:]
    return s
