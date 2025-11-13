import math

def jump_search(arr, target):
    """
    Поиск скачками (Jump Search) в отсортированном массиве
    
    Args:
        arr: отсортированный список элементов
        target: элемент, который нужно найти
    
    Returns:
        Индекс элемента, если найден, иначе -1
    """
    
    n = len(arr)
    
    # Проверка на пустой массив
    if n == 0:
        return -1
    
    print(f"Массив: {arr}")
    print(f"Ищем: {target}")
    print(f"Длина массива: {n}")
    
    # Вычисляем оптимальный размер прыжка - квадратный корень из длины массива
    step = int(math.sqrt(n))
    print(f"Размер прыжка (step): {step}")
    print()
    
    # ШАГ 1: Поиск блока, где может находиться элемент
    print("ШАГ 1: Поиск нужного блока")
    prev = 0
    
    # Прыгаем вперед, пока не найдем блок, где arr[min(step, n)-1] >= target
    while arr[min(step, n) - 1] < target:
        print(f"Прыжок: проверяем индекс {min(step, n) - 1}, значение = {arr[min(step, n) - 1]}")
        prev = step
        step += int(math.sqrt(n))
        
        # Если вышли за границы массива - элемент не найден
        if prev >= n:
            print("Вышли за границы массива - элемент не найден")
            return -1
    
    print(f"Найден блок: индексы от {prev} до {min(step, n) - 1}")
    print(f"Значения в блоке: {arr[prev:min(step, n)]}")
    print()
    
    # ШАГ 2: Линейный поиск в найденном блоке
    print("ШАГ 2: Линейный поиск в блоке")
    
    while arr[prev] < target:
        print(f"Проверяем индекс {prev}, значение = {arr[prev]}")
        prev += 1
        
        # Если дошли до конца блока или массива - элемент не найден
        if prev == min(step, n):
            print("Достигнут конец блока - элемент не найден")
            return -1
    
    # Проверяем, нашли ли мы нужный элемент
    if arr[prev] == target:
        print(f"Элемент найден! Индекс: {prev}, значение: {arr[prev]}")
        return prev
    else:
        print(f"Элемент не найден. На индексе {prev} значение {arr[prev]}")
        return -1


def jump_search_optimized(arr, target):
    """
    Оптимизированная версия поиска скачками
    """
    n = len(arr)
    if n == 0:
        return -1
    
    # Определяем размер прыжка
    step = int(math.sqrt(n))
    
    # Поиск блока
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Линейный поиск в блоке
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
        if arr[i] > target:
            break
    
    return -1


def jump_search_with_custom_step(arr, target, step_size=None):
    """
    Поиск скачками с возможностью указать размер прыжка
    
    Args:
        arr: отсортированный список
        target: искомый элемент
        step_size: размер прыжка (если None, вычисляется автоматически)
    """
    n = len(arr)
    if n == 0:
        return -1
    
    # Если размер прыжка не указан, вычисляем оптимальный
    if step_size is None:
        step_size = int(math.sqrt(n))
    elif step_size <= 0:
        raise ValueError("Размер прыжка должен быть положительным числом")
    
    print(f"Поиск с размером прыжка: {step_size}")
    
    # Поиск блока
    prev = 0
    current_step = step_size
    
    while current_step <= n and arr[current_step - 1] < target:
        prev = current_step
        current_step += step_size
    
    # Линейный поиск в блоке
    for i in range(prev, min(current_step, n)):
        if arr[i] == target:
            return i
        if arr[i] > target:
            break
    
    return -1


# Демонстрация работы алгоритма
if __name__ == "__main__":
    print("=" * 70)
    print("ПОИСК СКАЧКАМИ (JUMP SEARCH) - ДЕМОНСТРАЦИЯ")
    print("=" * 70)
    
    # Тестовый отсортированный массив
    test_arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    
    # Тест 1: Поиск существующего элемента
    print("\n" + "=" * 50)
    print("ТЕСТ 1: ПОИСК СУЩЕСТВУЮЩЕГО ЭЛЕМЕНТА")
    print("=" * 50)
    
    target1 = 55
    result1 = jump_search(test_arr, target1)
    print(f"\nРезультат: индекс {result1}")
    print(f"Проверка: test_arr[{result1}] = {test_arr[result1]}")
    
    # Тест 2: Поиск несуществующего элемента
    print("\n" + "=" * 50)
    print("ТЕСТ 2: ПОИСК НЕСУЩЕСТВУЮЩЕГО ЭЛЕМЕНТА")
    print("=" * 50)
    
    target2 = 100
    result2 = jump_search(test_arr, target2)
    print(f"\nРезультат: {result2}")
    
    # Тест 3: Поиск первого элемента
    print("\n" + "=" * 50)
    print("ТЕСТ 3: ПОИСК ПЕРВОГО ЭЛЕМЕНТА")
    print("=" * 50)
    
    target3 = 0
    result3 = jump_search(test_arr, target3)
    print(f"\nРезультат: индекс {result3}")
    
    # Тест 4: Поиск последнего элемента
    print("\n" + "=" * 50)
    print("ТЕСТ 4: ПОИСК ПОСЛЕДНЕГО ЭЛЕМЕНТА")
    print("=" * 50)
    
    target4 = 610
    result4 = jump_search(test_arr, target4)
    print(f"\nРезультат: индекс {result4}")
    
    # Тест 5: Оптимизированная версия
    print("\n" + "=" * 50)
    print("ТЕСТ 5: ОПТИМИЗИРОВАННАЯ ВЕРСИЯ")
    print("=" * 50)
    
    target5 = 34
    result5 = jump_search_optimized(test_arr, target5)
    print(f"Ищем {target5}, найдено на индексе: {result5}")
    
    # Тест 6: Поиск с кастомным размером прыжка
    print("\n" + "=" * 50)
    print("ТЕСТ 6: ПОИСК С КАСТОМНЫМ РАЗМЕРОМ ПРЫЖКА")
    print("=" * 50)
    
    target6 = 21
    result6 = jump_search_with_custom_step(test_arr, target6, step_size=5)
    print(f"Ищем {target6}, найдено на индексе: {result6}")


# Сравнение с другими алгоритмами поиска
def compare_search_algorithms(arr, target):
    """
    Сравнение поиска скачками с линейным и бинарным поиском
    """
    import time
    
    print(f"\nСравнение алгоритмов поиска для массива длиной {len(arr)}")
    print(f"Ищем элемент: {target}")
    
    # Линейный поиск
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            linear_result = i
            break
    else:
        linear_result = -1
    linear_time = time.time() - start_time
    
    # Бинарный поиск
    start_time = time.time()
    left, right = 0, len(arr) - 1
    binary_result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            binary_result = mid
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    binary_time = time.time() - start_time
    
    # Поиск скачками
    start_time = time.time()
    jump_result = jump_search_optimized(arr, target)
    jump_time = time.time() - start_time
    
    print(f"\nРезультаты:")
    print(f"Линейный поиск: индекс {linear_result}, время: {linear_time:.6f} сек")
    print(f"Бинарный поиск: индекс {binary_result}, время: {binary_time:.6f} сек")
    print(f"Поиск скачками: индекс {jump_result}, время: {jump_time:.6f} сек")
    
    return linear_result, binary_result, jump_result


# Демонстрация сравнения
print("\n" + "=" * 70)
print("СРАВНЕНИЕ АЛГОРИТМОВ ПОИСКА")
print("=" * 70)

test_arr_large = list(range(0, 1000, 2))  # Четные числа от 0 до 998
compare_search_algorithms(test_arr_large, 256)


# Дополнительная функция для визуализации процесса
def visualize_jump_search(arr, target):
    """
    Визуализация процесса поиска скачками
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    print("Визуализация поиска скачками:")
    print("Индексы: " + " ".join(f"{i:2}" for i in range(n)))
    print("Значения: " + " ".join(f"{x:2}" for x in arr))
    print()
    
    # Фаза прыжков
    current_step = step
    while current_step <= n and arr[current_step - 1] < target:
        print(f"Прыжок: проверяем индекс {current_step - 1} (значение {arr[current_step - 1]})")
        prev = current_step
        current_step += step
    
    print(f"Блок найден: индексы {prev}-{min(current_step, n) - 1}")
    
    # Линейный поиск
    found = False
    for i in range(prev, min(current_step, n)):
        marker = "← НАЙДЕН!" if arr[i] == target else ""
        print(f"Линейный поиск: индекс {i}, значение {arr[i]} {marker}")
        if arr[i] == target:
            found = True
            break
        if arr[i] > target:
            break
    
    if not found:
        print("Элемент не найден")

# Демонстрация визуализации
print("\n" + "=" * 70)
print("ВИЗУАЛИЗАЦИЯ ПРОЦЕССА")
print("=" * 70)

small_test_arr = [2, 5, 8, 12, 16, 23, 38, 45, 67, 73, 89, 91]
visualize_jump_search(small_test_arr, 45)