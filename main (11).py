import math

def exponential_search(arr, target):
    """
    Экспоненциальный поиск (Exponential Search) в отсортированном массиве
    
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
    
    # ШАГ 1: Проверка первого элемента
    print("ШАГ 1: Проверка первого элемента")
    if arr[0] == target:
        print(f"Элемент найден в начале! Индекс: 0")
        return 0
    elif arr[0] > target:
        print(f"Первый элемент {arr[0]} уже больше искомого {target}")
        return -1
    else:
        print(f"Первый элемент {arr[0]} меньше искомого {target}, продолжаем поиск")
    print()
    
    # ШАГ 2: Экспоненциальное расширение диапазона
    print("ШАГ 2: Экспоненциальное расширение диапазона")
    i = 1
    while i < n and arr[i] <= target:
        print(f"Проверяем индекс {i}, значение = {arr[i]}")
        if arr[i] == target:
            print(f"Элемент найден при экспоненциальном расширении! Индекс: {i}")
            return i
        i *= 2
        print(f"Увеличиваем диапазон: следующий индекс для проверки = {i}")
    
    # Определяем границы для бинарного поиска
    left = i // 2  # Начало диапазона
    right = min(i, n - 1)  # Конец диапазона
    
    print(f"\nОпределен диапазон для бинарного поиска:")
    print(f"left = {left}, right = {right}")
    print(f"Подмассив: {arr[left:right+1]}")
    print()
    
    # ШАГ 3: Бинарный поиск в найденном диапазоне
    print("ШАГ 3: Бинарный поиск в диапазоне")
    return binary_search_in_range(arr, target, left, right)


def binary_search_in_range(arr, target, left, right):
    """
    Вспомогательная функция для бинарного поиска в заданном диапазоне
    """
    print(f"Бинарный поиск в диапазоне [{left}, {right}]")
    
    while left <= right:
        mid = left + (right - left) // 2
        print(f"left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        
        if arr[mid] == target:
            print(f"Элемент найден! Индекс: {mid}")
            return mid
        elif arr[mid] < target:
            print(f"arr[mid] = {arr[mid]} < {target}, ищем в правой половине")
            left = mid + 1
        else:
            print(f"arr[mid] = {arr[mid]} > {target}, ищем в левой половине")
            right = mid - 1
    
    print("Элемент не найден в диапазоне")
    return -1


def exponential_search_optimized(arr, target):
    """
    Оптимизированная версия экспоненциального поиска
    """
    n = len(arr)
    if n == 0:
        return -1
    
    # Проверка первого элемента
    if arr[0] == target:
        return 0
    
    # Экспоненциальное расширение
    i = 1
    while i < n and arr[i] <= target:
        if arr[i] == target:
            return i
        i *= 2
    
    # Бинарный поиск в диапазоне
    return binary_search(arr, target, i // 2, min(i, n - 1))


def binary_search(arr, target, left, right):
    """
    Стандартный бинарный поиск
    """
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def exponential_search_unbounded(arr, target, get_func=None):
    """
    Экспоненциальный поиск для массивов с неизвестным размером
    или с ограниченным доступом к элементам
    
    Args:
        arr: массив или функция доступа к элементам (опционально)
        target: искомый элемент
        get_func: функция для получения элемента по индексу (опционально)
    """
    if get_func is None:
        # Если передан обычный массив
        get_func = lambda idx: arr[idx] if idx < len(arr) else float('inf')
        n = len(arr)
    else:
        # Если размер неизвестен, ищем верхнюю границу
        n = find_upper_bound(get_func, target)
    
    # Стандартный экспоненциальный поиск
    return exponential_search_optimized_with_getter(get_func, target, n)


def find_upper_bound(get_func, target):
    """
    Находит верхнюю границу для массива с неизвестным размером
    """
    i = 1
    while get_func(i) != float('inf') and get_func(i) <= target:
        i *= 2
    return i


def exponential_search_optimized_with_getter(get_func, target, n):
    """
    Экспоненциальный поиск с функцией доступа к элементам
    """
    if get_func(0) == target:
        return 0
    
    i = 1
    while i < n and get_func(i) <= target:
        if get_func(i) == target:
            return i
        i *= 2
    
    # Бинарный поиск в диапазоне
    left = i // 2
    right = min(i, n - 1)
    
    while left <= right:
        mid = left + (right - left) // 2
        mid_val = get_func(mid)
        
        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


# Демонстрация работы алгоритма
if __name__ == "__main__":
    print("=" * 70)
    print("ЭКСПОНЕНЦИАЛЬНЫЙ ПОИСК (EXPONENTIAL SEARCH) - ДЕМОНСТРАЦИЯ")
    print("=" * 70)
    
    # Тестовый отсортированный массив
    test_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    
    # Тест 1: Поиск существующего элемента в середине
    print("\n" + "=" * 50)
    print("ТЕСТ 1: ПОИСК ЭЛЕМЕНТА В СЕРЕДИНЕ")
    print("=" * 50)
    
    target1 = 17
    result1 = exponential_search(test_arr, target1)
    print(f"\nФинальный результат: индекс {result1}")
    print(f"Проверка: test_arr[{result1}] = {test_arr[result1]}")
    
    # Тест 2: Поиск несуществующего элемента
    print("\n" + "=" * 50)
    print("ТЕСТ 2: ПОИСК НЕСУЩЕСТВУЮЩЕГО ЭЛЕМЕНТА")
    print("=" * 50)
    
    target2 = 16
    result2 = exponential_search(test_arr, target2)
    print(f"\nФинальный результат: {result2}")
    
    # Тест 3: Поиск первого элемента
    print("\n" + "=" * 50)
    print("ТЕСТ 3: ПОИСК ПЕРВОГО ЭЛЕМЕНТА")
    print("=" * 50)
    
    target3 = 1
    result3 = exponential_search(test_arr, target3)
    print(f"\nФинальный результат: индекс {result3}")
    
    # Тест 4: Поиск последнего элемента
    print("\n" + "=" * 50)
    print("ТЕСТ 4: ПОИСК ПОСЛЕДНЕГО ЭЛЕМЕНТА")
    print("=" * 50)
    
    target4 = 31
    result4 = exponential_search(test_arr, target4)
    print(f"\nФинальный результат: индекс {result4}")
    
    # Тест 5: Оптимизированная версия
    print("\n" + "=" * 50)
    print("ТЕСТ 5: ОПТИМИЗИРОВАННАЯ ВЕРСИЯ")
    print("=" * 50)
    
    target5 = 13
    result5 = exponential_search_optimized(test_arr, target5)
    print(f"Ищем {target5}, найдено на индексе: {result5}")
    
    # Тест 6: Поиск в очень большом массиве
    print("\n" + "=" * 50)
    print("ТЕСТ 6: ПОИСК В БОЛЬШОМ МАССИВЕ")
    print("=" * 50)
    
    large_arr = list(range(0, 1000000, 2))  # Четные числа до 2 миллионов
    target6 = 123456
    result6 = exponential_search_optimized(large_arr, target6)
    print(f"Массив из {len(large_arr)} элементов")
    print(f"Ищем {target6}, найдено на индексе: {result6}")
    if result6 != -1:
        print(f"Проверка: large_arr[{result6}] = {large_arr[result6]}")


# Сравнение с другими алгоритмами поиска
def compare_search_algorithms(arr, target):
    """
    Сравнение экспоненциального поиска с другими алгоритмами
    """
    import time
    
    print(f"\nСравнение алгоритмов поиска для массива длиной {len(arr)}")
    print(f"Ищем элемент: {target}")
    
    # Линейный поиск
    start_time = time.time()
    linear_result = -1
    for i in range(len(arr)):
        if arr[i] == target:
            linear_result = i
            break
    linear_time = time.time() - start_time
    
    # Бинарный поиск
    start_time = time.time()
    binary_result = binary_search(arr, target, 0, len(arr) - 1)
    binary_time = time.time() - start_time
    
    # Экспоненциальный поиск
    start_time = time.time()
    exp_result = exponential_search_optimized(arr, target)
    exp_time = time.time() - start_time
    
    print(f"\nРезультаты:")
    print(f"Линейный поиск: индекс {linear_result}, время: {linear_time:.6f} сек")
    print(f"Бинарный поиск:  индекс {binary_result}, время: {binary_time:.6f} сек")
    print(f"Экспоненциальный: индекс {exp_result}, время: {exp_time:.6f} сек")
    
    return linear_result, binary_result, exp_result


# Демонстрация сравнения
print("\n" + "=" * 70)
print("СРАВНЕНИЕ АЛГОРИТМОВ ПОИСКА")
print("=" * 70)

test_arr_medium = list(range(0, 10000, 1))
compare_search_algorithms(test_arr_medium, 5678)


# Дополнительная функция для поиска в бесконечном массиве
class InfiniteArray:
    """
    Класс для имитации бесконечного отсортированного массива
    """
    def __init__(self, real_array=None):
        self.real_array = real_array or []
        self.access_count = 0
    
    def __getitem__(self, idx):
        self.access_count += 1
        if idx < len(self.real_array):
            return self.real_array[idx]
        else:
            return float('inf')  # За пределами реального массива
    
    def get_access_count(self):
        return self.access_count


def demo_infinite_array_search():
    """
    Демонстрация поиска в "бесконечном" массиве
    """
    print("\n" + "=" * 70)
    print("ПОИСК В БЕСКОНЕЧНОМ МАССИВЕ")
    print("=" * 70)
    
    # Создаем "бесконечный" массив
    finite_data = list(range(0, 1000, 2))  # Четные числа до 2000
    infinite_arr = InfiniteArray(finite_data)
    
    target = 456
    print(f"Ищем {target} в 'бесконечном' массиве")
    
    # Используем экспоненциальный поиск
    result = exponential_search_unbounded(None, target, lambda idx: infinite_arr[idx])
    
    print(f"Результат: индекс {result}")
    print(f"Количество обращений к массиву: {infinite_arr.get_access_count()}")
    if result != -1:
        print(f"Проверка: значение = {finite_data[result]}")


# Запуск демонстрации
demo_infinite_array_search()


# Визуализация процесса поиска
def visualize_exponential_search(arr, target):
    """
    Визуализация процесса экспоненциального поиска
    """
    n = len(arr)
    print("Визуализация экспоненциального поиска:")
    print("Индексы: " + " ".join(f"{i:3}" for i in range(min(n, 20))))
    print("Значения: " + " ".join(f"{arr[i]:3}" for i in range(min(n, 20))))
    if n > 20:
        print(f"... (массив продолжается до индекса {n-1})")
    print()
    
    # Проверка первого элемента
    if arr[0] == target:
        print("✓ Найден на индексе 0!")
        return 0
    
    # Экспоненциальное расширение
    i = 1
    steps = []
    while i < n and arr[i] <= target:
        steps.append(i)
        if arr[i] == target:
            print(f"✓ Найден при экспоненциальном расширении на индексе {i}!")
            return i
        i *= 2
    
    left = i // 2
    right = min(i, n - 1)
    
    print(f"Экспоненциальное расширение: проверены индексы {steps}")
    print(f"Диапазон для бинарного поиска: [{left}, {right}]")
    print()
    
    # Бинарный поиск
    while left <= right:
        mid = (left + right) // 2
        arrow = " ← НАЙДЕН!" if arr[mid] == target else ""
        print(f"Бинарный поиск: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}{arrow}")
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    print("✗ Элемент не найден")
    return -1


# Демонстрация визуализации
print("\n" + "=" * 70)
print("ВИЗУАЛИЗАЦИЯ ПРОЦЕССА")
print("=" * 70)

small_test_arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
visualize_exponential_search(small_test_arr, 18)