from array_list import ArrayList
from stack import Stack
import random


def binary_search(arr, value, start, end):
    left = start
    right = end
    last = start
    while left < right:
        mid = (left + right) // 2
        if value < arr.get(mid):
            right = mid - 1
        elif value >= arr.get(mid):
            left = mid + 1
            last = mid
    return last


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
    lcount = rcount = 0
    while i < left.size and j < right.size:
        if lcount == 7:
            lcount = 0
            g = i - 1
            gi = 0
            while g < left.size and i < right.size and left.get(g) <= right.get(j):
                g = min(i - 1 + 2 ** gi, left.size - 1)
                gi += 1
                if g == left.size - 1:
                    break
            index = binary_search(left, right.get(j), i, g)
            if index and i < index:
                for i in range(i, index + 1):
                    arr.set(k, left.get(i))
                    k += 1
                i += 1
        elif rcount == 7:
            rcount = 0
            g = j - 1
            gi = 0
            while i < left.size and g < right.size and left.get(i) >= right.get(g):
                g = min(j - 1 + 2 ** gi, right.size - 1)
                gi += 1
                if g == right.size - 1:
                    break
            index = binary_search(right, left.get(i), j, g)
            if index and j < index:
                for j in range(j, index + 1):
                    arr.set(k, right.get(j))
                    k += 1
                j += 1
        if i < left.size and j < right.size:
            if left.get(i) <= right.get(j):
                arr.set(k, left.get(i))
                i += 1
                lcount += 1
                rcount = 0
            else:
                arr.set(k, right.get(j))
                j += 1
                rcount += 1
                lcount = 0
            k += 1

    while i < left.size:
        arr.set(k, left.get(i))
        k += 1
        i += 1

    while j < right.size:
        arr.set(k, right.get(j))
        k += 1
        j += 1


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
    if len(runs_above) > 1:
        x = runs_above[0]
        y = runs_above[1]
        if len(runs_above) == 2:
            if not y[1] > x[1] or last:
                merge(arr, y[0], y[0] + y[1] - 1, x[0] + x[1] - 1)
                runs_stack.push([y[0], y[1] + x[1]])
            else:
                runs_stack.push(y)
                runs_stack.push(x)
        elif len(runs_above) == 3:
            z = runs_above[2]
            if not (z[1] > y[1] + x[1] and y[1] > x[1]):
                if z[1] > x[1]:
                    merge(arr, y[0], y[0] + y[1] - 1, x[0] + x[1] - 1)
                    runs_stack.push(z)
                    runs_stack.push([y[0], y[1] + x[1]])
                else:
                    merge(arr, z[0], z[0] + z[1] - 1, y[0] + y[1] - 1)
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
    print("minrun:", minrun)
    runs_stack = Stack()
    find_runs(arr, minrun, runs_stack)
    while merge_runs(arr, runs_stack, 1):
        pass


if __name__ == '__main__':
    for N in range(100, 10000, 150):
        print("N: ", N)
        arr = ArrayList(N)
        arr1 = ArrayList(N)
        for i in range(N):
            intgr = random.randint(1, 100)
            arr.add(intgr)
            arr1.add(intgr)
        timsort(arr)
        arr.print()
        arr1.sort()
        arr1.print()
        assert arr1.array == arr.array, True