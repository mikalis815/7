def ternary_search(arr, target):
    """
    Тернарный поиск в отсортированном массиве
    
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
    print()
    
    def _ternary_search(left, right, depth=0):
        """
        Внутренняя рекурсивная функция для тернарного поиска
        """
        indent = "  " * depth
        print(f"{indent}Глубина {depth}: поиск в диапазоне [{left}, {right}]")
        
        # Базовый случай - диапазон слишком мал
        if left > right:
            print(f"{indent}Диапазон пуст - элемент не найден")
            return -1
        
        # Вычисляем две точки деления
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        print(f"{indent}Точки деления: mid1={mid1}, mid2={mid2}")
        print(f"{indent}Значения: arr[{mid1}]={arr[mid1]}, arr[{mid2}]={arr[mid2]}")
        
        # Проверяем точки деления
        if arr[mid1] == target:
            print(f"{indent}✓ Найден в mid1={mid1}!")
            return mid1
        
        if arr[mid2] == target:
            print(f"{indent}✓ Найден в mid2={mid2}!")
            return mid2
        
        # Определяем в какой трети продолжать поиск
        if target < arr[mid1]:
            print(f"{indent}target < arr[{mid1}] → ищем в левой трети [{left}, {mid1-1}]")
            return _ternary_search(left, mid1 - 1, depth + 1)
        elif target > arr[mid2]:
            print(f"{indent}target > arr[{mid2}] → ищем в правой трети [{mid2+1}, {right}]")
            return _ternary_search(mid2 + 1, right, depth + 1)
        else:
            print(f"{indent}arr[{mid1}] < target < arr[{mid2}] → ищем в средней трети [{mid1+1}, {mid2-1}]")
            return _ternary_search(mid1 + 1, mid2 - 1, depth + 1)
    
    return _ternary_search(0, n - 1)


def ternary_search_iterative(arr, target):
    """
    Итеративная версия тернарного поиска
    """
    n = len(arr)
    if n == 0:
        return -1
    
    left, right = 0, n - 1
    step = 0
    
    print(f"Итеративный тернарный поиск: {target} в массиве длиной {n}")
    
    while left <= right:
        step += 1
        print(f"\nШаг {step}: диапазон [{left}, {right}]")
        
        # Вычисляем точки деления
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        print(f"  Точки деления: mid1={mid1}, mid2={mid2}")
        print(f"  Значения: arr[{mid1}]={arr[mid1]}, arr[{mid2}]={arr[mid2]}")
        
        # Проверяем точки деления
        if arr[mid1] == target:
            print(f"  ✓ Найден в mid1={mid1}!")
            return mid1
        
        if arr[mid2] == target:
            print(f"  ✓ Найден в mid2={mid2}!")
            return mid2
        
        # Определяем следующую область поиска
        if target < arr[mid1]:
            print(f"  target < arr[{mid1}] → сужаем к левой трети")
            right = mid1 - 1
        elif target > arr[mid2]:
            print(f"  target > arr[{mid2}] → сужаем к правой трети")
            left = mid2 + 1
        else:
            print(f"  arr[{mid1}] < target < arr[{mid2}] → сужаем к средней трети")
            left = mid1 + 1
            right = mid2 - 1
    
    print(f"Элемент не найден после {step} шагов")
    return -1


def ternary_search_unimodal(func, left, right, eps=1e-9, find_max=True):
    """
    Тернарный поиск для нахождения экстремума унимодальной функции
    
    Args:
        func: унимодальная функция
        left, right: границы поиска
        eps: точность
        find_max: если True - ищем максимум, иначе минимум
    
    Returns:
        x: точка экстремума
    """
    
    print(f"Тернарный поиск {'максимума' if find_max else 'минимума'}")
    print(f"Диапазон: [{left}, {right}], точность: {eps}")
    print()
    
    iteration = 0
    
    while right - left > eps:
        iteration += 1
        
        # Вычисляем две точки деления
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        
        # Вычисляем значения функции в точках деления
        f_mid1 = func(mid1)
        f_mid2 = func(mid2)
        
        print(f"Итерация {iteration}:")
        print(f"  Диапазон: [{left:.6f}, {right:.6f}]")
        print(f"  Точки: m1={mid1:.6f}, m2={mid2:.6f}")
        print(f"  Значения: f(m1)={f_mid1:.6f}, f(m2)={f_mid2:.6f}")
        
        if find_max:
            # Для максимума
            if f_mid1 < f_mid2:
                print(f"  f(m1) < f(m2) → сужаем к правой части")
                left = mid1
            else:
                print(f"  f(m1) >= f(m2) → сужаем к левой части")
                right = mid2
        else:
            # Для минимума
            if f_mid1 > f_mid2:
                print(f"  f(m1) > f(m2) → сужаем к правой части")
                left = mid1
            else:
                print(f"  f(m1) <= f(m2) → сужаем к левой части")
                right = mid2
        
        print(f"  Новый диапазон: [{left:.6f}, {right:.6f}]")
        print()
    
    result = (left + right) / 2
    print(f"Найден {'максимум' if find_max else 'минимум'} в точке x = {result:.8f}")
    print(f"f(x) = {func(result):.8f}")
    print(f"Потребовалось итераций: {iteration}")
    
    return result


# Демонстрация работы алгоритма
if __name__ == "__main__":
    print("=" * 70)
    print("ТЕРНАРНЫЙ ПОИСК (TERNARY SEARCH) - ДЕМОНСТРАЦИЯ")
    print("=" * 70)
    
    # Тест 1: Рекурсивный поиск в массиве
    print("\n" + "=" * 50)
    print("ТЕСТ 1: РЕКУРСИВНЫЙ ПОИСК В МАССИВЕ")
    print("=" * 50)
    
    test_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    target1 = 17
    result1 = ternary_search(test_arr, target1)
    print(f"\nФинальный результат: индекс {result1}")
    print(f"Проверка: test_arr[{result1}] = {test_arr[result1]}")
    
    # Тест 2: Итеративный поиск
    print("\n" + "=" * 50)
    print("ТЕСТ 2: ИТЕРАТИВНЫЙ ПОИСК")
    print("=" * 50)
    
    target2 = 13
    result2 = ternary_search_iterative(test_arr, target2)
    print(f"\nФинальный результат: индекс {result2}")
    
    # Тест 3: Поиск несуществующего элемента
    print("\n" + "=" * 50)
    print("ТЕСТ 3: ПОИСК НЕСУЩЕСТВУЮЩЕГО ЭЛЕМЕНТА")
    print("=" * 50)
    
    target3 = 16
    result3 = ternary_search_iterative(test_arr, target3)
    print(f"\nФинальный результат: {result3}")
    
    # Тест 4: Поиск минимума функции
    print("\n" + "=" * 50)
    print("ТЕСТ 4: ПОИСК МИНИМУМА ФУНКЦИИ")
    print("=" * 50)
    
    # Функция: парабола f(x) = (x-3)^2 + 2
    def parabola(x):
        return (x - 3) ** 2 + 2
    
    min_point = ternary_search_unimodal(parabola, 0, 6, eps=1e-6, find_max=False)
    print(f"\nТеоретический минимум: x = 3.0, f(x) = 2.0")
    
    # Тест 5: Поиск максимума функции
    print("\n" + "=" * 50)
    print("ТЕСТ 5: ПОИСК МАКСИМУМА ФУНКЦИИ")
    print("=" * 50)
    
    # Функция: -парабола f(x) = -(x-2)^2 + 5
    def negative_parabola(x):
        return -(x - 2) ** 2 + 5
    
    max_point = ternary_search_unimodal(negative_parabola, 0, 4, eps=1e-6, find_max=True)
    print(f"\nТеоретический максимум: x = 2.0, f(x) = 5.0")


# Сравнение с бинарным поиском
def compare_ternary_binary(arr, target):
    """
    Сравнение тернарного и бинарного поиска
    """
    import time
    
    print(f"\nСравнение алгоритмов поиска для массива длиной {len(arr)}")
    print(f"Ищем элемент: {target}")
    
    # Бинарный поиск
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        comparisons = 0
        
        while left <= right:
            comparisons += 1
            mid = (left + right) // 2
            
            if arr[mid] == target:
                return mid, comparisons
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1, comparisons
    
    # Тернарный поиск (итеративный)
    def ternary_search_count(arr, target):
        left, right = 0, len(arr) - 1
        comparisons = 0
        
        while left <= right:
            comparisons += 2  # Два сравнения на шаг
            
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3
            
            if arr[mid1] == target:
                return mid1, comparisons
            if arr[mid2] == target:
                return mid2, comparisons
            
            if target < arr[mid1]:
                right = mid1 - 1
            elif target > arr[mid2]:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1
        
        return -1, comparisons
    
    # Замер времени и сравнений
    start_time = time.time()
    bin_result, bin_comparisons = binary_search(arr, target)
    bin_time = time.time() - start_time
    
    start_time = time.time()
    tern_result, tern_comparisons = ternary_search_count(arr, target)
    tern_time = time.time() - start_time
    
    print(f"\nРезультаты:")
    print(f"Бинарный поиск:   индекс {bin_result}, сравнений {bin_comparisons}, время {bin_time:.6f} сек")
    print(f"Тернарный поиск:  индекс {tern_result}, сравнений {tern_comparisons}, время {tern_time:.6f} сек")
    
    # Анализ эффективности
    n = len(arr)
    print(f"\nТеоретическая сложность:")
    print(f"Бинарный поиск: O(log₂{n}) ≈ {math.log2(n):.1f} шагов")
    print(f"Тернарный поиск: O(log₃{n}) ≈ {math.log(n, 3):.1f} шагов")
    
    return bin_result, tern_result


# Демонстрация сравнения
print("\n" + "=" * 70)
print("СРАВНЕНИЕ ТЕРНАРНОГО И БИНАРНОГО ПОИСКА")
print("=" * 70)

import math
test_arr_large = list(range(0, 10000))
compare_ternary_binary(test_arr_large, 5678)


# Дополнительные примеры унимодальных функций
def demo_unimodal_functions():
    """
    Демонстрация поиска экстремумов различных унимодальных функций
    """
    print("\n" + "=" * 70)
    print("ПОИСК ЭКСТРЕМУМОВ РАЗЛИЧНЫХ ФУНКЦИЙ")
    print("=" * 70)
    
    # Пример 1: Синусоида с шумом
    print("\n1. ФУНКЦИЯ: f(x) = -sin(x) + 0.1*x (поиск минимума)")
    def sin_function(x):
        return -math.sin(x) + 0.1 * x
    
    min_sin = ternary_search_unimodal(sin_function, 0, 2 * math.pi, eps=1e-6, find_max=False)
    
    # Пример 2: Кубическая функция
    print("\n2. ФУНКЦИЯ: f(x) = -(x-1)**3 + 3*(x-1)**2 (поиск максимума)")
    def cubic_function(x):
        return -(x - 1) ** 3 + 3 * (x - 1) ** 2
    
    max_cubic = ternary_search_unimodal(cubic_function, -1, 3, eps=1e-6, find_max=True)
    
    # Пример 3: Экспоненциальная функция
    print("\n3. ФУНКЦИЯ: f(x) = exp(-(x-2)**2) (поиск максимума)")
    def exp_function(x):
        return math.exp(-(x - 2) ** 2)
    
    max_exp = ternary_search_unimodal(exp_function, 0, 4, eps=1e-6, find_max=True)


# Запуск демонстрации с функциями
import math
demo_unimodal_functions()


# Визуализация процесса для малых массивов
def visualize_ternary_search_small():
    """
    Визуализация тернарного поиска на маленьком массиве
    """
    print("\n" + "=" * 70)
    print("ВИЗУАЛИЗАЦИЯ НА МАЛЕНЬКОМ МАССИВЕ")
    print("=" * 70)
    
    small_arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target = 12
    
    print(f"Массив: {small_arr}")
    print(f"Ищем: {target}")
    print()
    
    left, right = 0, len(small_arr) - 1
    step = 0
    
    while left <= right:
        step += 1
        print(f"Шаг {step}:")
        
        # Визуализация текущего диапазона
        range_str = ["  "] * len(small_arr)
        for i in range(left, right + 1):
            range_str[i] = "↑"
        print("Индексы: " + " ".join(f"{i:2}" for i in range(len(small_arr))))
        print("         " + " ".join(f"{s:2}" for s in range_str))
        print("Значения: " + " ".join(f"{x:2}" for x in small_arr))
        
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        print(f"Точки деления: mid1={mid1}, mid2={mid2}")
        print(f"Сравниваем: {target} с {small_arr[mid1]} и {small_arr[mid2]}")
        
        if small_arr[mid1] == target:
            print(f"✓ Найден на позиции {mid1}!")
            return mid1
        if small_arr[mid2] == target:
            print(f"✓ Найден на позиции {mid2}!")
            return mid2
        
        if target < small_arr[mid1]:
            print(f"{target} < {small_arr[mid1]} → левая треть")
            right = mid1 - 1
        elif target > small_arr[mid2]:
            print(f"{target} > {small_arr[mid2]} → правая треть")
            left = mid2 + 1
        else:
            print(f"{small_arr[mid1]} < {target} < {small_arr[mid2]} → средняя треть")
            left = mid1 + 1
            right = mid2 - 1
        
        print()
    
    print("Элемент не найден")
    return -1


# Демонстрация визуализации
visualize_ternary_search_small()