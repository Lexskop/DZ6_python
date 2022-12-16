# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]
from task5 import result

pair_numbers_multiple_5 = list(filter(lambda x: (x[0]+x[1])%5 == False, result))
print('\n'f'Результат 6-й задачи -> {pair_numbers_multiple_5}')