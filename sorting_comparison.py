import timeit
import random


# ============================================================
# Алгоритми сортування
# ============================================================

def merge_sort(arr):
    """Сортування злиттям — O(n log n)."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    """Злиття двох відсортованих масивів."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def insertion_sort(arr):
    """Сортування вставками — O(n^2)."""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ============================================================
# Вимірювання часу
# ============================================================

def measure_time(func, data, runs=5):
    """Вимірює час виконання функції через timeit."""
    timer = timeit.Timer(lambda: func(data.copy()))
    return timer.timeit(number=runs) / runs


def run_benchmark():
    """Запускає бенчмарк для різних розмірів масивів."""
    sizes = [100, 1000, 5000, 10000]

    print("=" * 65)
    print(f"  {'Розмір':<10} {'Злиттям':>14} {'Вставками':>14} {'Timsort':>14}")
    print("=" * 65)

    for size in sizes:
        data = [random.randint(1, 10000) for _ in range(size)]

        time_merge = measure_time(merge_sort, data)
        time_insertion = measure_time(insertion_sort, data)
        time_timsort = measure_time(sorted, data)

        print(f"  {size:<10} {time_merge:>13.6f}s {time_insertion:>13.6f}s {time_timsort:>13.6f}s")

    print("=" * 65)


if __name__ == "__main__":
    run_benchmark()