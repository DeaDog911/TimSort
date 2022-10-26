from array_list import ArrayList


def insert_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        value = arr.get(i)
        j = i - 1
        while j >= start and arr.get(j) > value:
            arr.set(j+1, arr.get(j))
            arr.set(j, value)
            j -= 1


def merge(arr, start, mid, end):
    len1, len2 = mid - start + 1, end - mid
    left = ArrayList(len1)
    right = ArrayList(len2)
    for i in range(0, len1):
        left.add(arr.get(start + i))
    for i in range(0, len2):
        right.add(arr.get(mid + 1 + i))
    i, j, k = 0, 0, start
    while i < left.size and j < right.size:
        if left.get(i) <= right.get(j):
            arr.set(k, left.get(i))
            i += 1
        else:
            arr.set(k, right.get(j))
            j += 1
        k += 1

    while i < left.size:
        arr.set(k, left.get(i))
        k += 1
        i += 1

    while j < right.size:
        arr.set(k, right.get(j))
        k += 1
        j += 1


def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)