def pancake_sort(arr):
    """
    Реализация блинной сортировки (pancake sort)
    
    Args:
        arr: список элементов для сортировки (должны поддерживать сравнение)
    
    Returns:
        Отсортированный список
    """
    
    # Создаем копию массива, чтобы не изменять оригинал
    arr = arr.copy()
    n = len(arr)
    
    print(f"Начальный массив: {arr}")
    print(f"Длина массива: {n}")
    print()
    
    # Проходим по массиву справа налево
    # На каждой итерации самый большой элемент будет перемещаться в конец
    for curr_size in range(n, 1, -1):
        print(f"=== Итерация {n - curr_size + 1} ===")
        print(f"Текущий размер неотсортированной части: {curr_size}")
        print(f"Текущее состояние массива: {arr}")
        
        # ШАГ 1: Находим индекс максимального элемента в неотсортированной части
        max_idx = find_max_index(arr, curr_size)
        print(f"Индекс максимального элемента ({arr[max_idx]}): {max_idx}")
        
        # Если максимальный элемент уже не на своем месте, выполняем перевороты
        if max_idx != curr_size - 1:
            # ШАГ 2: Переворачиваем массив до позиции максимального элемента
            # Это перемещает максимальный элемент в начало
            if max_idx != 0:
                print(f"Переворот 1: flip(arr, {max_idx + 1})")
                flip(arr, max_idx + 1)
                print(f"После первого переворота: {arr}")
            else:
                print("Максимальный элемент уже в начале, первый переворот не нужен")
            
            # ШАГ 3: Переворачиваем весь неотсортированный подмассив
            # Это перемещает максимальный элемент из начала в конец неотсортированной части
            print(f"Переворот 2: flip(arr, {curr_size})")
            flip(arr, curr_size)
            print(f"После второго переворота: {arr}")
        else:
            print("Максимальный элемент уже на своем месте, перевороты не нужны")
        
        print(f"Состояние после итерации: {arr}")
        print()
    
    print("Сортировка завершена!")
    return arr


def flip(arr, k):
    """
    Переворачивает первые k элементов массива
    
    Args:
        arr: массив для переворота
        k: количество элементов для переворота (от начала до k-1 индекса)
    """
    left = 0
    right = k - 1
    
    while left < right:
        # Меняем местами элементы
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def find_max_index(arr, n):
    """
    Находит индекс максимального элемента в первых n элементах массива
    
    Args:
        arr: массив для поиска
        n: количество элементов для поиска (от 0 до n-1)
    
    Returns:
        Индекс максимального элемента
    """
    max_idx = 0
    for i in range(1, n):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx


def pancake_sort_with_steps(arr):
    """
    Упрощенная версия блинной сортировки с минимальным выводом
    """
    arr = arr.copy()
    n = len(arr)
    
    print(f"Начальный массив: {arr}")
    
    for curr_size in range(n, 1, -1):
        max_idx = find_max_index(arr, curr_size)
        
        if max_idx != curr_size - 1:
            if max_idx != 0:
                flip(arr, max_idx + 1)
                print(f"Переворот до позиции {max_idx + 1}: {arr}")
            
            flip(arr, curr_size)
            print(f"Переворот до позиции {curr_size}: {arr}")
    
    print(f"Результат: {arr}")
    return arr


# Демонстрация работы алгоритма
if __name__ == "__main__":
    print("=" * 70)
    print("БЛИННАЯ СОРТИРОВКА - ДЕМОНСТРАЦИЯ")
    print("=" * 70)
    
    # Тест 1: Простой случай
    print("\n" + "=" * 50)
    print("ТЕСТ 1: ПРОСТОЙ СЛУЧАЙ")
    print("=" * 50)
    
    test_arr1 = [3, 1, 4, 2]
    print(f"Исходный массив: {test_arr1}")
    sorted_arr1 = pancake_sort(test_arr1)
    print(f"Финальный результат: {sorted_arr1}")
    print(f"Проверка сортировки: {sorted_arr1 == sorted(test_arr1)}")
    
    # Тест 2: Уже отсортированный массив
    print("\n" + "=" * 50)
    print("ТЕСТ 2: УЖЕ ОТСОРТИРОВАННЫЙ МАССИВ")
    print("=" * 50)
    
    test_arr2 = [1, 2, 3, 4, 5]
    print(f"Исходный массив: {test_arr2}")
    sorted_arr2 = pancake_sort(test_arr2)
    print(f"Финальный результат: {sorted_arr2}")
    print(f"Проверка сортировки: {sorted_arr2 == sorted(test_arr2)}")
    
    # Тест 3: Обратно отсортированный массив
    print("\n" + "=" * 50)
    print("ТЕСТ 3: ОБРАТНО ОТСОРТИРОВАННЫЙ МАССИВ")
    print("=" * 50)
    
    test_arr3 = [5, 4, 3, 2, 1]
    print(f"Исходный массив: {test_arr3}")
    sorted_arr3 = pancake_sort(test_arr3)
    print(f"Финальный результат: {sorted_arr3}")
    print(f"Проверка сортировки: {sorted_arr3 == sorted(test_arr3)}")
    
    # Тест 4: Случайные числа (упрощенный вывод)
    print("\n" + "=" * 50)
    print("ТЕСТ 4: СЛУЧАЙНЫЕ ЧИСЛА (УПРОЩЕННЫЙ ВЫВОД)")
    print("=" * 50)
    
    test_arr4 = [23, 10, 20, 11, 12, 6, 7]
    print(f"Исходный массив: {test_arr4}")
    sorted_arr4 = pancake_sort_with_steps(test_arr4)
    print(f"Проверка сортировки: {sorted_arr4 == sorted(test_arr4)}")


# Дополнительная функция для визуализации процесса
def visualize_pancake_sort(arr):
    """
    Визуализация процесса блинной сортировки
    """
    arr = arr.copy()
    n = len(arr)
    steps = []
    
    print("\nВИЗУАЛИЗАЦИЯ ПРОЦЕССА:")
    print(" " + " ".join(map(str, arr)))
    
    for curr_size in range(n, 1, -1):
        max_idx = find_max_index(arr, curr_size)
        
        if max_idx != curr_size - 1:
            if max_idx != 0:
                flip(arr, max_idx + 1)
                steps.append(f"flip({max_idx + 1})")
                print(" " + " ".join(map(str, arr)) + f"  ← {steps[-1]}")
            
            flip(arr, curr_size)
            steps.append(f"flip({curr_size})")
            print(" " + " ".join(map(str, arr)) + f"  ← {steps[-1]}")
    
    print(f"\nВсего шагов: {len(steps)}")
    print(f"Последовательность переворотов: {', '.join(steps)}")


# Демонстрация визуализации
print("\n" + "=" * 50)
print("ВИЗУАЛИЗАЦИЯ ПРОЦЕССА")
print("=" * 50)
test_visual = [3, 1, 4, 2]
visualize_pancake_sort(test_visual)