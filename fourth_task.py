"""Из-за того, что в задании не указывается,
что четвёртое задание должно быть выполненно в консоли,
то использование сторонних библеотек для визуализации не будет считаться ошибкой"""

from matplotlib import pyplot as plt


def ratio():
    print("Задание 4: Диаграмма\n")
    # Set of numbers 1
    SON1 = 0
    # Set of numbers 2
    SON2 = 0
    with open('sequence.txt') as numb:
        massiv = [float(i) for i in numb.read().split()]
    for i in range(len(massiv)):
        if 0 <= massiv[i] <= 5:
            SON1 += 1
        elif 0 >= massiv[i] >= -5:
            SON2 += 2
    print('Множество чисел от 0 до 5 = ', SON1)
    print('Множество чисел от -5 до 0 = ', SON2, '\n')
    print("Соотношение множеств: ")
    if SON1 <= SON2:
        p = SON1 / (SON2 + SON1) * 100
        print(p, '% |', 100 - p, '%', '\n')
    else:
        p = SON2 / (SON1 + SON2) * 100
        print(p, '% |', 100 - p, '%', '\n')
    sets = ['Числа от 0 до 5', 'Числа от -5 до 0']

    data = [SON1, SON2]

    plt.figure(figsize=(10, 7))
    plt.pie(data, labels=sets, autopct='%1.2f%%')
    plt.show()
