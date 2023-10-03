"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
"""


def total_cranes(num):
    petya = serezha = total_cranes_input / 6
    katya = 2 * (petya + serezha)
    return petya, katya, serezha


total_cranes_input = int(input("Введите общее число сделанных из бумаг журавликов: "))

petya, katya, serezha = total_cranes(total_cranes_input)

print("Петя: ", int(petya), "Катя: ", int(katya), "Сережа: ", int(serezha))
