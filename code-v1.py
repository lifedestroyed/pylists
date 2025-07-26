# Created by lifedestroyed. https://github.com/lifedestroyed/pylists/

def task_3_1():
    lst = [1, 2, 3, 4, 5]
    print("Положительные индексы:", lst[0], lst[2], lst[:3])
    print("Отрицательные индексы:", lst[-5], lst[-3], lst[-5:-2])

def task_3_2():
    lst = [[1, 2, ['Ok!', 3]], ['list', 4], 5]
    print(lst[0][2][0])

def task_3_3():
    lst = [42, [3.14, [1j, ['string', []]]]]
    print(lst[1][1][1][0])

def task_3_4():
    lst = ['Санкт', '+', 'Петербург']
    lst[1] = '-'
    print(''.join(lst))

def task_3_5():
    lst = ['a', '1', 'b', '2', 'c', '3']
    letters = [x for i, x in enumerate(lst) if i % 2 == 0]
    numbers = [x for i, x in enumerate(lst) if i % 2 != 0]
    print("Буквы:", letters)
    print("Цифры:", numbers)

def task_3_6():
    lst = [1, 2, 3, 4, 5]
    lst[:3] = [sum(lst[:3])]
    lst.append(7)
    lst.insert(-2, lst.pop(0))
    print(lst)

def task_3_7():
    lst = [3, 4, 1, 1, 5, 1]
    print(f"Всего элементов: {len(lst)}, Количество единиц: {lst.count(1)}, Индекс первой единицы: {lst.index(1)}")

def task_3_8():
    lst = []
    lst.append('a')
    lst.append('b')
    lst.extend(['c', 'e'])
    lst.insert(3, 'd')
    print(lst)

def task_3_9():
    lst = ['a', 'b', 'c', 'd', 'e']
    lst.pop()
    lst.reverse()
    lst.remove('c')
    lst.clear()
    print("Очищенный список:", lst)

def task_3_10():
    lst = [3, -54, 25, 8, 0]
    print(f"Сумма: {sum(lst)}, Разность max и min: {max(lst) - min(lst)}")

def task_3_11():
    lst = [7, 7, -4, 2.5, -.9, 0]
    print(f"Количество отрицательных элементов: {sum(1 for x in lst if x < 0)}")

def task_3_12():
    lst = [0.3, -2.4, 4.5, 0.0, -3.1]
    print(f"Индекс минимального элемента: {lst.index(min(lst))}")

def task_3_13():
    lst = [9, -3, 5, 0, -3]
    print(f"Сумма модулей: {sum(abs(x) for x in lst)}")

def task_3_14():
    lst = [9, -210, 0, 500, -37]
    min_idx, max_idx = lst.index(min(lst)), lst.index(max(lst))
    lst[min_idx], lst[max_idx] = lst[max_idx], lst[min_idx]
    print(lst)

def task_3_15():
    lst = [3, 2, 3, 2, 1, 4]
    lst.sort(reverse=True)
    lst.append(len(lst))
    print(lst)

def task_3_16():
    lst = [True, 5, 'go', 3+0.1j]
    lst.insert(0, lst.pop())
    print(lst)

def task_3_17():
    lst = [13, 5, 5, 8, 16, 4]
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            del lst[i]
            break
    print(lst)

def task_3_18():
    lst = ['уж', 'змея', '', 'питон']
    lst = [x for x in lst if len(x) >= 5]
    print(lst)

def task_3_19():
    lst = ['три', [2, 5], 0.7, 'home']
    print([type(x).__name__ for x in lst])

def task_3_20():
    lst = [1.0, 'ok', True, 'ok', 7, 1]
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    print(result)

def task_3_21():
    lst1 = ['1', 'True', 'ok']
    lst2 = ['no', 'True', 'no']
    print(list(set(lst1).union(set(lst2))))

def task_3_22():
    lst = [1, None, 3.0, [1, 2], 'b']
    for i in range(0, len(lst)-1, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]
    print(lst)

def show_menu():
    print()
    print("="*50)
    print("МЕНЮ ПРОГРАММЫ".center(50))
    print("="*50)
    print("1. Задача 3.1 - Индексация и срезы")
    print("2. Задача 3.2 - Вложенные списки")
    print("3. Задача 3.3 - Список-матрешка")
    print("4. Задача 3.4 - Изменение элемента")
    print("5. Задача 3.5 - Разделение списка")
    print("6. Задача 3.6 - Модификация списка")
    print("7. Задача 3.7 - Статистика списка")
    print("8. Задача 3.8 - Добавление элементов")
    print("9. Задача 3.9 - Удаление элементов")
    print("10. Задача 3.10 - Сумма и разность")
    print("11. Задача 3.11 - Отрицательные элементы")
    print("12. Задача 3.12 - Индекс минимума")
    print("13. Задача 3.13 - Сумма модулей")
    print("14. Задача 3.14 - Обмен min и max")
    print("15. Задача 3.15 - Сортировка и длина")
    print("16. Задача 3.16 - Циклический сдвиг")
    print("17. Задача 3.17 - Удаление по условию")
    print("18. Задача 3.18 - Фильтрация строк")
    print("19. Задача 3.19 - Типы элементов")
    print("20. Задача 3.20 - Удаление дублей")
    print("21. Задача 3.21 - Объединение списков")
    print("22. Задача 3.22 - Обмен соседей")
    print("0. Выход")
    print("="*50)

def main():
    tasks = {
        1: task_3_1, 2: task_3_2, 3: task_3_3, 4: task_3_4, 5: task_3_5,
        6: task_3_6, 7: task_3_7, 8: task_3_8, 9: task_3_9, 10: task_3_10,
        11: task_3_11, 12: task_3_12, 13: task_3_13, 14: task_3_14, 15: task_3_15,
        16: task_3_16, 17: task_3_17, 18: task_3_18, 19: task_3_19, 20: task_3_20,
        21: task_3_21, 22: task_3_22
    }

    while True:
        show_menu()
        try:
            choice = int(input("Выберите задачу (0-22): "))
            if choice == 0:
                print("Выход из программы...")
                break
            elif 1 <= choice <= 22:
                print()
                print(f"Задача 3.{choice}:")
                tasks[choice]()
                print()
                input("Нажмите Enter чтобы продолжить...")
            else:
                print("Ошибка: введите число от 0 до 22")
        except ValueError:
            print("Ошибка: введите корректное число")

if __name__ == "__main__":
    main()
