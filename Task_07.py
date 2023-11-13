"""Задача №7. Решение в группах
Дано натуральное число. Требуется определить,
является ли год с данным номером високосным. Если
год является високосным, то выведите YES, иначе
выведите NO. Напомним, что в соответствии с
григорианским календарем, год является
високосным, если его номер кратен 4, но не кратен
100, а также если он кратен 400.
Input: 2016
Output: YES
"""

# решение 1
year = 2025
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("YES")
else:
    print("NO")

# решение 2 через тернарный оператор
print("YES" if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else "NO")
