from array_list import ArrayList
from stack import Stack
import random


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
    while i < len1 and j < len2:
        if left.get(i) <= right.get(j):
            arr.set(k, left.get(i))
            i += 1
        else:
            arr.set(k, right.get(j))
            j += 1
        k += 1
    while i < len1:
        arr.set(k, left.get(i))
        k += 1
        i += 1
    while j < len2:
        arr.set(k, right.get(j))
        k += 1
        j += 1


def merge_gallop(arr, start, mid, end):
    len1, len2 = mid - start + 1, end - mid
    left = ArrayList(len1)
    right = ArrayList(len2)
    for i in range(0, len1):
        left.add(arr.get(start + i))
    for i in range(0, len2):
        right.add(arr.get(mid + 1 + i))
    i, j, k = 0, 0, start
    lcount = rcount = 0
    while i < len1 and j < len2:
        if left.get(i) <= right.get(j):
            arr.set(k, left.get(i))
            i += 1
        else:
            arr.set(k, right.get(j))
            j += 1
        k += 1
    while i < len1:
        arr.set(k, left.get(i))
        k += 1
        i += 1
    while j < len2:
        arr.set(k, right.get(j))
        k += 1
        j += 1


def merge_sort(arr, start, end):
    if start < end:
        mid = (end + start) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


def get_minrun(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r


def reverse(arr, start, end):
    i = start
    j = end
    while i < j:
        value = arr.get(i)
        arr.set(i, arr.get(j))
        arr.set(j, value)
        i += 1
        j -= 1


def merge_runs(arr, runs_stack, last = 0):
    runs_above = []
    while runs_stack.peek() and len(runs_above) < 3:
        runs_above.append(runs_stack.pop().data)
    print(runs_above)
    if len(runs_above) > 1:
        x = runs_above[0]
        y = runs_above[1]
        if len(runs_above) == 2:
            if not y[1] > x[1] or last:
                merge_gallop(arr, y[0], y[0] + y[1] - 1, x[0] + x[1] - 1)
                runs_stack.push([y[0], y[1] + x[1]])
            else:
                runs_stack.push(y)
                runs_stack.push(x)
        elif len(runs_above) == 3:
            z = runs_above[2]
            if not (z[1] > y[1] + x[1] and y[1] > x[1]):
                if z[1] > x[1]:
                    merge_gallop(arr, y[0], y[0] + y[1] - 1, x[0] + x[1] - 1)
                    runs_stack.push(z)
                    runs_stack.push([y[0], y[1] + x[1]])
                else:
                    merge_gallop(arr, z[0], z[0] + z[1] - 1, y[0] + y[1] - 1)
                    runs_stack.push([z[0], z[1] + y[1]])
                    runs_stack.push(x)
            else:
                runs_stack.push(z)
                runs_stack.push(y)
                runs_stack.push(x)
    else:
        runs_stack.push(runs_above[0])
        return False
    return True


def find_runs(arr, minrun, runs_stack):
    index = 0
    while index < arr.size-1:
        start = index
        if arr.get(index) <= arr.get(index + 1):
            run_type = 0
        else:
            run_type = 1
        index += 2
        index = min(arr.size-1, index + minrun - 3)
        if index + 2 * minrun > arr.size:
            index = arr.size - 1
        if run_type == 1:
            reverse(arr, start, index)
        insert_sort(arr, start, index)
        runs_stack.push([start, index - start + 1])
        merge_runs(arr, runs_stack)
        index += 1


def timsort(arr: ArrayList):
    N = arr.size
    minrun = get_minrun(N)
    print(minrun)
    runs_stack = Stack()
    find_runs(arr, minrun, runs_stack)
    while merge_runs(arr, runs_stack, 1):
        pass


if __name__ == '__main__':
    N = 100
    arr = ArrayList(N)
    arr1 = ArrayList(N)
    j = 1
    for i in range(N):
        intgr = j
        arr.add(intgr)
        arr1.add(intgr)
        j += 1
    timsort(arr)
    arr.print()
    arr1.sort()
    arr1.print()
    print(arr1.array == arr.array)