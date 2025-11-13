def bead_sort(arr):
    """
    Реализация сортировки бусинами (гравитационной сортировки)
    
    Args:
        arr: список неотрицательных целых чисел для сортировки
    
    Returns:
        Отсортированный список (по убыванию)
    
    Важно: 
        - Работает только с неотрицательными целыми числами
        - Возвращает массив, отсортированный по убыванию
        - Для получения возрастающего порядка нужно перевернуть результат
    """
    
    # Проверка на пустой массив или массив с одним элементом
    if len(arr) <= 1:
        return arr.copy()
    
    # Проверка, что все элементы неотрицательные целые числа
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("Сортировка бусинами работает только с неотрицательными целыми числами")
    
    print(f"Начальный массив: {arr}")
    print(f"Максимальное значение: {max(arr)}")
    print(f"Длина массива: {len(arr)}")
    print()
    
    # ШАГ 1: Создаем "абак" - матрицу для представления бусин
    max_val = max(arr)
    n = len(arr)
    
    # Создаем матрицу размером max_val x n, заполненную нулями
    # Каждая строка представляет уровень, каждый столбец - число
    beads = [[0] * n for _ in range(max_val)]
    
    print("ШАГ 1: Размещаем бусины на абаке")
    print("(1 - бусина, 0 - пустое место)")
    visualize_beads(beads, arr)
    
    # Размещаем бусины согласно исходному массиву
    for i, value in enumerate(arr):
        for j in range(value):
            beads[j][i] = 1
    
    print("После размещения бусин:")
    visualize_beads(beads, arr)
    
    # ШАГ 2: Моделируем "падение" бусин под действием гравитации
    print("\nШАГ 2: Моделируем падение бусин под действием гравитации")
    
    for level in range(max_val):
        print(f"\nУровень {level}:")
        
        # Для каждого столбца считаем, сколько бусин должно упасть
        for col in range(n):
            if beads[level][col] == 1:
                # Бусина падает вниз - ищем самую нижнюю свободную позицию в этом столбце
                beads[level][col] = 0
                fall_distance = 0
                
                # Ищем, на сколько позиций может упасть бусина
                for fall_level in range(level, -1, -1):
                    if fall_level == 0 or beads[fall_level-1][col] == 1:
                        fall_distance = level - fall_level
                        break
                
                if fall_distance > 0:
                    # Перемещаем бусину вниз
                    beads[level - fall_distance][col] = 1
                    print(f"  Бусина в столбце {col} упала на {fall_distance} позиций")
        
        visualize_beads(beads, arr)
    
    # ШАГ 3: Считываем результат
    print("\nШАГ 3: Считываем отсортированный массив")
    sorted_arr = []
    
    for col in range(n):
        # Считаем количество бусин в каждом столбце
        count = 0
        for level in range(max_val):
            if beads[level][col] == 1:
                count += 1
        sorted_arr.append(count)
    
    print(f"Отсортированный массив (по убыванию): {sorted_arr}")
    
    # Для получения возрастающего порядка переворачиваем массив
    sorted_arr_asc = sorted_arr[::-1]
    print(f"Отсортированный массив (по возрастанию): {sorted_arr_asc}")
    
    return sorted_arr


def bead_sort_optimized(arr):
    """
    Оптимизированная версия сортировки бусинами
    Более эффективная реализация
    """
    if len(arr) <= 1:
        return arr.copy()
    
    # Проверка на неотрицательные целые числа
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("Сортировка бусинами работает только с неотрицательными целыми числами")
    
    max_val = max(arr)
    
    # Создаем и инициализируем абак
    beads = [[0] * len(arr) for _ in range(max_val)]
    
    # Размещаем бусины
    for i, value in enumerate(arr):
        for j in range(value):
            beads[j][i] = 1
    
    # Моделируем падение (оптимизированная версия)
    for level in range(max_val):
        # Считаем количество бусин на каждом уровне
        bead_count = sum(beads[level])
        
        # Распределяем бусины по столбцам (все падают влево)
        for col in range(len(arr)):
            if col < bead_count:
                beads[level][col] = 1
            else:
                beads[level][col] = 0
    
    # Считываем результат
    sorted_arr = []
    for col in range(len(arr)):
        count = sum(1 for level in range(max_val) if beads[level][col] == 1)
        sorted_arr.append(count)
    
    return sorted_arr[::-1]  # Возвращаем по возрастанию


def bead_sort_simple(arr):
    """
    Простая версия сортировки бусинами
    Легче для понимания
    """
    if not arr:
        return []
    
    max_val = max(arr)
    
    # Создаем абак
    beads = [[0] * len(arr) for _ in range(max_val)]
    
    # Расставляем бусины
    for i, num in enumerate(arr):
        for j in range(num):
            beads[j][i] = 1
    
    # Падение бусин - все бусины "падают" влево
    for i in range(max_val):
        # Считаем бусины в строке
        count = sum(beads[i])
        # Все бусины сдвигаются влево
        beads[i] = [1] * count + [0] * (len(arr) - count)
    
    # Считываем результат
    result = []
    for j in range(len(arr)):
        result.append(sum(1 for i in range(max_val) if beads[i][j] == 1))
    
    return result[::-1]


def visualize_beads(beads, original_arr=None):
    """
    Визуализация текущего состояния абакa
    """
    if not beads:
        return
    
    rows = len(beads)
    cols = len(beads[0]) if beads else 0
    
    print("   " + " ".join(str(i).rjust(2) for i in range(cols)))
    print("  " + "---" * cols)
    
    for i in range(rows-1, -1, -1):
        row_str = f"{i:2}|"
        for j in range(cols):
            if beads[i][j] == 1:
                row_str += " ● "
            else:
                row_str += " ○ "
        print(row_str)
    
    if original_arr is not None:
        print("   " + " ".join(str(x).rjust(2) for x in original_arr))
    
    print()


# Демонстрация работы алгоритма
if __name__ == "__main__":
    print("=" * 70)
    print("СОРТИРОВКА БУСИНАМИ (ГРАВИТАЦИОННАЯ) - ДЕМОНСТРАЦИЯ")
    print("=" * 70)
    
    # Тест 1: Простой случай
    print("\n" + "=" * 50)
    print("ТЕСТ 1: ПРОСТОЙ СЛУЧАЙ")
    print("=" * 50)
    
    test_arr1 = [3, 1, 4, 2]
    print(f"Исходный массив: {test_arr1}")
    sorted_arr1 = bead_sort(test_arr1)
    print(f"Проверка сортировки: {sorted_arr1 == [1, 2, 3, 4]}")
    
    # Тест 2: Оптимизированная версия
    print("\n" + "=" * 50)
    print("ТЕСТ 2: ОПТИМИЗИРОВАННАЯ ВЕРСИЯ")
    print("=" * 50)
    
    test_arr2 = [5, 2, 7, 1, 3]
    print(f"Исходный массив: {test_arr2}")
    sorted_arr2 = bead_sort_optimized(test_arr2)
    print(f"Результат: {sorted_arr2}")
    print(f"Проверка сортировки: {sorted_arr2 == sorted(test_arr2)}")
    
    # Тест 3: Простая версия
    print("\n" + "=" * 50)
    print("ТЕСТ 3: ПРОСТАЯ ВЕРСИЯ")
    print("=" * 50)
    
    test_arr3 = [2, 4, 1, 3, 2]
    print(f"Исходный массив: {test_arr3}")
    sorted_arr3 = bead_sort_simple(test_arr3)
    print(f"Результат: {sorted_arr3}")
    print(f"Проверка сортировки: {sorted_arr3 == sorted(test_arr3)}")
    
    # Тест 4: С нулевыми значениями
    print("\n" + "=" * 50)
    print("ТЕСТ 4: С НУЛЕВЫМИ ЗНАЧЕНИЯМИ")
    print("=" * 50)
    
    test_arr4 = [3, 0, 2, 0, 4]
    print(f"Исходный массив: {test_arr4}")
    sorted_arr4 = bead_sort_simple(test_arr4)
    print(f"Результат: {sorted_arr4}")
    print(f"Проверка сортировки: {sorted_arr4 == sorted(test_arr4)}")


# Дополнительная функция для анимации процесса
def bead_sort_animation(arr, delay=0.5):
    """
    Упрощенная анимация процесса сортировки
    """
    import time
    
    if len(arr) <= 1:
        return arr
    
    max_val = max(arr)
    beads = [[0] * len(arr) for _ in range(max_val)]
    
    # Исходное размещение
    for i, value in enumerate(arr):
        for j in range(value):
            beads[j][i] = 1
    
    print("Начальное состояние:")
    visualize_beads(beads, arr)
    time.sleep(delay)
    
    # Процесс "падения"
    for level in range(max_val):
        bead_count = sum(beads[level])
        new_row = [1] * bead_count + [0] * (len(arr) - bead_count)
        
        if beads[level] != new_row:
            beads[level] = new_row
            print(f"Уровень {level} после падения:")
            visualize_beads(beads, arr)
            time.sleep(delay)
    
    # Финальный результат
    result = []
    for col in range(len(arr)):
        count = sum(1 for level in range(max_val) if beads[level][col] == 1)
        result.append(count)
    
    return result[::-1]

# Тест анимации (раскомментируйте для демонстрации)
# print("\nАНИМАЦИЯ ПРОЦЕССА:")
# test_anim = [2, 4, 1, 3]
# bead_sort_animation(test_anim, delay=1)