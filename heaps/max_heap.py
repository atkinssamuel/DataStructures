import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

heap_dir = "heaps/"

def get_parent(index):
    return math.floor((index - 1)/2)

def get_left(index):
    return 2 * index + 1

def get_right(index):
    return 2 * index + 2


def max_heapify(array, index):
    left = get_left(index)
    right = get_right(index)

    largest = index

    if left < len(array) and array[left] > array[largest]:
        largest = left

    if right < len(array) and array[right] > array[largest]:
        largest = right

    if largest != index:
        temp = array[index]
        array[index] = array[largest]
        array[largest] = temp
        array = max_heapify(array, largest)

    return array


def create_max_heap(array):
    # The index of the last element in the array is len(array)-1
    # The formula for the parent node is floor((child_index - 1)/2)
    # half_index = math.floor((len(array)-2) / 2)
    half_index = get_parent(len(array) - 1)

    for i in range(half_index, -1, -1):
        array = max_heapify(array, i)

    return array

def insert_max_heap(array, element):
    array.append(element)

    current_index = len(array) - 1
    parent_index = get_parent(current_index)

    while current_index != 0:
        if array[current_index] > array[parent_index]:
            array[current_index], array[parent_index] = array[parent_index], array[current_index]
            current_index = parent_index
            parent_index = get_parent(current_index)
        else:
            return array

    return array

def extract_max_heap(array):
    value = array[0]
    array[0] = array[len(array) - 1]
    array.pop()

    array = max_heapify(array, 0)
    return array, value

def print_heap(array):
    print("Heap:")
    # Height of heap: h = ceil(log2(N+1)-1)
    height = math.ceil(math.log2(len(array) + 1) - 1)
    for i in range(height + 1):
        j = 0
        tier = []
        while j < math.pow(2, i) and j + math.pow(2, i) - 1 < len(array):
            tier.append(array[int(j + math.pow(2, i)-1)])
            j += 1
        print(tier)


if __name__ == "__main__":
    original_heap = Image.open(heap_dir + "original_heap.PNG")
    plt.imshow(original_heap)

    original_heap_array = [0, 5, 4, 6, 1, 7, 2, 8]

    print("\nOriginal Heap:")
    print_heap(original_heap_array)

    print("\nMax Heap:")
    max_heap = create_max_heap(original_heap_array)
    print_heap(max_heap)

    print("\nInsert 9:")
    max_heap = insert_max_heap(max_heap, 9)
    print_heap(max_heap)

    print("\nExtract Element:")
    max_heap, return_element = extract_max_heap(max_heap)
    print("Return Element:", return_element)
    print_heap(max_heap)


