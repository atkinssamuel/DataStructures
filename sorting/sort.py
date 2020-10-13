import numpy as np
import math
import time
# List of sorting algorithms:
# Selection sort, bubble sort, insertion sort, merge sort, quick sort, heap sort

'''
def quickSort(array):
    if len(array) == 1:
        return

    pivot = math.floor(len(array)/2)
    array[pivot], array[len(array) - 1] = array[len(array) - 1], array[pivot]

    itemFromLeft = -1
    itemFromRight = -1

    right_index = len(array) - 2

    for i in range(len(array)):
        if itemFromLeft != -1:
            if array[i] > array[pivot]:
                itemFromLeft = i

        if itemFromRight != -1:
            if array[right_index] < array[pivot]:
                itemFromRight = right_index
        if itemFromRight != -1 and itemFromRight != -1:
            break
        right_index -= 1

    if itemFromLeft < itemFromRight:
        array[itemFromLeft], array[itemFromRight] = array[itemFromRight], array[itemFromLeft]
    else:
        array[pivot], array[itemFromLeft] = array[itemFromLeft], array[pivot]
'''

def selection_sort(array):
    k = 0
    while k < len(array) - 1:
        mindex = k
        for i in range(k, len(array)):
            if array[i] < array[mindex]:
                mindex = i
        array[mindex], array[k] = array[k], array[mindex]
        k += 1

    return array


def selection_sort_recursive(array, k):
    # Base case is when len(array) == 1
    if k == len(array) - 1:
        return array
    mindex = k
    for i in range(k, len(array)):
        if array[i] < array[mindex]:
            mindex = i
    array[k], array[mindex] = array[mindex], array[k]

    return selection_sort_recursive(array, k+1)


def bubble_sort(array):
    k = len(array)
    while k > 1:
        for i in range(k-1):
            if array[i+1] < array[i]:
                array[i], array[i+1] = array[i+1], array[i]
        k -= 1
    return array


def insertion_sort(array):
    for i in range(len(array)):
        for j in range(i):
            if array[i] > array[j] and array[i] < array[j+1]:
                temp = array[j]
                array[j] = array[i]
                array[j+1:] = [temp, array[]]



if __name__ == "__main__":
    scrambled_list = [2, 4, 1, 6, 8, 5, 3, 7]

    start_time = time.time()
    selection_sort_result = selection_sort(scrambled_list)
    print("\nSelection sort result:", selection_sort_result)
    print(f"Time to run = {round(time.time() - start_time, 10)}s")

    start_time = time.time()
    selection_sort_recursive_result = selection_sort_recursive(scrambled_list, 0)
    print("\nSelection sort recurisve result:", selection_sort_recursive_result)
    print(f"Time to run = {round(time.time() - start_time, 10)}s")

    start_time = time.time()
    bubble_sort_result = bubble_sort(scrambled_list)
    print("\nBubble sort result:", bubble_sort_result)
    print(f"Time to run = {round(time.time() - start_time, 10)}s")

    start_time = time.time()
    insertion_sort_result = insertion_sort(scrambled_list)
    print("\nInsertion sort result:", insertion_sort_result)
    print(f"Time to run = {round(time.time() - start_time, 10)}s")
