def bucket_sort(arr, bucket_size=5):
    """
    Реализация блочной (корзинной) сортировки
    
    Args:
        arr: список чисел для сортировки
        bucket_size: размер каждой корзины (определяет диапазон значений в одной корзине)
    
    Returns:
        Отсортированный список
    """
    
    # Проверка на пустой массив или массив с одним элементом
    if len(arr) <= 1:
        return arr.copy()
    
    # ШАГ 1: Определяем диапазон значений и количество корзин
    min_val = min(arr)
    max_val = max(arr)
    
    # Вычисляем количество корзин и преобразуем в целое число
    bucket_count = int((max_val - min_val) // bucket_size) + 1
    
    # Создаем пустые корзины (списки)
    buckets = [[] for _ in range(bucket_count)]
    
    print(f"Диапазон значений: [{min_val}, {max_val}]")
    print(f"Количество корзин: {bucket_count} (размер корзины: {bucket_size})")
    
    # ШАГ 2: Распределяем элементы по корзинам
    for num in arr:
        # Вычисляем индекс корзины для текущего элемента
        index = int((num - min_val) // bucket_size)
        
        # Убеждаемся, что индекс находится в допустимых пределах
        index = max(0, min(index, bucket_count - 1))
        
        # Помещаем элемент в соответствующую корзину
        buckets[index].append(num)
    
    # Выводим информацию о распределении по корзинам
    print("\nРаспределение элементов по корзинам:")
    for i, bucket in enumerate(buckets):
        range_start = min_val + i * bucket_size
        range_end = min_val + (i + 1) * bucket_size
        print(f"Корзина {i}: [{range_start:.2f}, {range_end:.2f}) - {len(bucket)} элементов: {bucket}")
    
    # ШАГ 3: Сортируем каждую корзину индивидуально
    print("\nПроцесс сортировки корзин:")
    for i in range(bucket_count):
        if buckets[i]:  # Сортируем только непустые корзины
            print(f"Корзина {i} до сортировки: {buckets[i]}")
            buckets[i] = insertion_sort(buckets[i])
            print(f"Корзина {i} после сортировки: {buckets[i]}")
    
    # ШАГ 4: Объединяем отсортированные корзины в правильном порядке
    result = []
    for i in range(bucket_count):
        result.extend(buckets[i])
    
    return result


def insertion_sort(arr):
    """
    Сортировка вставками для сортировки отдельных корзин
    """
    if len(arr) <= 1:
        return arr
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr


def bucket_sort_float(arr, num_buckets=10):
    """
    Специальная версия для сортировки чисел с плавающей точкой в диапазоне [0, 1)
    """
    if len(arr) <= 1:
        return arr.copy()
    
    # Создаем корзины
    buckets = [[] for _ in range(num_buckets)]
    
    # Распределяем элементы по корзинам
    for num in arr:
        index = int(num * num_buckets)
        # Обрабатываем случай, когда num = 1.0
        if index == num_buckets:
            index = num_buckets - 1
        buckets[index].append(num)
    
    # Сортируем каждую корзину
    for i in range(num_buckets):
        if buckets[i]:
            buckets[i].sort()
    
    # Объединяем результаты
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result


# Демонстрация работы алгоритма
if __name__ == "__main__":
    print("=" * 70)
    print("БЛОЧНАЯ (КОРЗИННАЯ) СОРТИРОВКА - ДЕМОНСТРАЦИЯ")
    print("=" * 70)
    
    # Тест 1: Целые числа с равномерным распределением
    print("\n" + "=" * 50)
    print("ТЕСТ 1: ЦЕЛЫЕ ЧИСЛА С РАВНОМЕРНЫМ РАСПРЕДЕЛЕНИЕМ")
    print("=" * 50)
    
    test_arr1 = [29, 25, 3, 49, 9, 37, 21, 43, 15, 8]
    print(f"Исходный массив: {test_arr1}")
    
    sorted_arr1 = bucket_sort(test_arr1, bucket_size=10)
    print(f"\nРезультат сортировки: {sorted_arr1}")
    print(f"Проверка сортировки: {sorted_arr1 == sorted(test_arr1)}")
    
    # Тест 2: Дробные числа (ИСПРАВЛЕННАЯ ВЕРСИЯ)
    print("\n" + "=" * 50)
    print("ТЕСТ 2: ДРОБНЫЕ ЧИСЛА")
    print("=" * 50)
    
    test_arr2 = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51, 0.29, 0.68, 0.75]
    print(f"Исходный массив: {test_arr2}")
    
    # Используем bucket_size=0.1 (теперь это работает!)
    sorted_arr2 = bucket_sort(test_arr2, bucket_size=0.1)
    print(f"\nРезультат сортировки: {sorted_arr2}")
    print(f"Проверка сортировки: {sorted_arr2 == sorted(test_arr2)}")
    
    # Тест 3: Специальная версия для чисел [0, 1)
    print("\n" + "=" * 50)
    print("ТЕСТ 3: СПЕЦИАЛЬНАЯ ВЕРСИЯ ДЛЯ ЧИСЕЛ [0, 1)")
    print("=" * 50)
    
    test_arr3 = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print(f"Исходный массив: {test_arr3}")
    
    sorted_arr3 = bucket_sort_float(test_arr3, num_buckets=5)
    print(f"Результат сортировки: {sorted_arr3}")
    print(f"Проверка сортировки: {sorted_arr3 == sorted(test_arr3)}")
    
    # Тест 4: Отрицательные числа
    print("\n" + "=" * 50)
    print("ТЕСТ 4: ОТРИЦАТЕЛЬНЫЕ ЧИСЛА")
    print("=" * 50)
    
    test_arr4 = [-5, 3, -2, 8, -1, 4, 0, -3, 7, 2]
    print(f"Исходный массив: {test_arr4}")
    
    sorted_arr4 = bucket_sort(test_arr4, bucket_size=3)
    print(f"Результат сортировки: {sorted_arr4}")
    print(f"Проверка сортировки: {sorted_arr4 == sorted(test_arr4)}")