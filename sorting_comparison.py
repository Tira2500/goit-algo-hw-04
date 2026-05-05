# Алгоритми сортування: злиттям, вставками та Timsort


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


if __name__ == "__main__":
    test = [64, 34, 25, 12, 22, 11, 90]
    print("Вихідний масив  :", test)
    print("Злиттям         :", merge_sort(test))
    print("Вставками       :", insertion_sort(test))
    print("Timsort (sorted):", sorted(test))
