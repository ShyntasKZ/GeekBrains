"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

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
