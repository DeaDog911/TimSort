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


def find_runs(arr, minrun, runs_stack):
    index = 0
    while index < arr.size:
        run = ArrayList()
        start = index
        run.add(arr.get(index))
        run.add(arr.get(index + 1))
        index += 2
        if run.get(0) <= run.get(1):
            run_type = 0
        else:
            run_type = 1
        while index < arr.size:
            if (run_type == 0 and arr.get(index - 1) <= arr.get(index)) \
                    or (run_type == 1 and arr.get(index - 1) > arr.get(index)):
                run.add(arr.get(index))
            else:
                break
            index += 1
        if run_type == 1:
            run.reverse()
        if run.size < minrun:
            run_size = run.size
            for index in range(index, index + (minrun - run_size)):
                run.add(arr.get(index))
            if index + minrun > arr.size:
                while index < arr.size-1:
                    run.add(arr.get(index))
                    index += 1
        run.print()
        insert_sort(run, 0, run.size-1)
        i = 0
        for k in range(start, start + run.size):
            arr.set(k, run.get(i))
            i += 1
        runs_stack.push([start, run.size])
        index += 1


def mergeRuns(arr, first_run, second_run):
    bigger_run = first_run if first_run[1] > second_run[1] else second_run
    smaller_run = first_run if first_run[1] < second_run[1] else second_run
    temp = ArrayList(smaller_run[1])
    for i in range(smaller_run[1]):
        temp.add(arr.get(i + smaller_run[0]))
    temp2 = ArrayList(bigger_run[1])
    for i in range(bigger_run[1]):
        temp2.add(arr.get(i + bigger_run[0]))
    start = min(smaller_run[0], bigger_run[0])
    k = start
    i = 0
    j = 0
    while (i < temp.size) and j < temp2.size:
        if temp.get(i) < temp2.get(j):
            arr.set(k, temp.get(i))
            i += 1
        else:
            arr.set(k, temp2.get(j))
            j += 1
        k += 1

    while i < temp.size:
        arr.set(k, temp.get(i))
        i += 1
        k += 1
    while j < temp2.size:
        arr.set(k, temp2.get(j))
        j += 1
        k += 1


def merge_runs(arr: ArrayList, runs_stack: Stack):
    while(runs_stack.peek()):
        runs_above = []
        i = 0
        while runs_stack.peek() and i < 3:
            runs_above.append(runs_stack.pop().data)
            i += 1
        if len(runs_above) == 3:
            if runs_above[2][1] <= runs_above[0][1] + runs_above[1][1]:
                if runs_above[0][1] < runs_above[2][1]:
                    mergeRuns(arr, runs_above[1], runs_above[0])
                else:
                    mergeRuns(arr, runs_above[1], runs_above[2])
        elif len(runs_above) == 2:
            if runs_above[0][1] <= runs_above[1][1]:
                mergeRuns(arr, runs_above[0], runs_above[1])
        #merge(arr, runs_above[0], runs_above[1])



def timsort(arr: ArrayList):
    N = arr.size
    minrun = get_minrun(N)
    runs_stack = Stack()
    find_runs(arr, minrun, runs_stack)
    merge_runs(arr, runs_stack)


if __name__ == '__main__':
    arr = ArrayList()
    for i in range(100):
        arr.add(random.randint(1, 100))
    arr.print()
    timsort(arr)
    arr.print()
    arr.sort()
    arr.print()