"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""


def total_cranes(num):
    petya = serezha = total_cranes_input / 6
    katya = 2 * (petya + serezha)
    return petya, katya, serezha


total_cranes_input = int(input("Введите общее число сделанных из бумаг журавликов: "))

petya, katya, serezha = total_cranes(total_cranes_input)

print("Петя: ", int(petya), "Катя: ", int(katya), "Сережа: ", int(serezha))
