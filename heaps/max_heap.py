import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

heap_dir = "heaps/"


def max_heapify(array, index, N):
    left = 2 * index + 1
    right = 2 * index + 2

    largest = index

    if left < N and array[left] > array[largest]:
        largest = left

    if right < N and array[right] > array[largest]:
        largest = right

    if largest != index:
        temp = array[index]
        array[index] = array[largest]
        array[largest] = temp
        array = max_heapify(array, largest, N)

    return array


def create_max_heap(array):
    N = len(original_heap_array)

    half_index = math.floor(N / 2)

    for i in range(half_index, -1, -1):
        array = max_heapify(array, i, N)

    return array


def print_heap(array):
    print("\nHeap:")
    for i in range(math.floor(len(array) / 2)):
        j = 0
        tier = []
        while j < math.pow(2, i) and j + math.pow(2, i) < len(array):
            tier.append(array[int(j + math.pow(2, i) - 1)])
            j += 1
        print(tier)


if __name__ == "__main__":
    original_heap = Image.open(heap_dir + "original_heap.PNG")
    plt.imshow(original_heap)

    original_heap_array = [0, 5, 4, 6, 1, 7, 2]
    print_heap(original_heap_array)

    max_heap = create_max_heap(original_heap_array)

    print_heap(max_heap)
