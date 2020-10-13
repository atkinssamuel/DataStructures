# Sorting Algorithms

### Selection Sort
#### Algorithm
Find the minimum element in i -> len(array) and swap that element with the element at i. Then, increment i and repeat until i == len(array).
#### Runtime
O(N^2)

### Bubble Sort
#### Algorithm
Keep track of the limiting index that starts at len(array). For i in range(len(array)), compare the element at i and the element at i + 1, if the element at i is greater than the element at i + 1, swap them. Once you have reached the limiting index, decrement the limiting index as the greatest element in the list will now be at the end of the list.
#### Runtime
O(N^2)

### Insertion Sort
#### Algorithm
This algorithm works in the same way that a person sorts cards in their hands. For each element in the array, insert that element in the sorted list prior to those elements. 
#### Runtime
O(N^2)

### Merge Sort
#### Algorithm
This algorithm is a divide and conquer algorithm. This algorithm takes the original array and then partitions it into multiple lists, each containing a single element. These lists are considered "sorted" because any list with just one element is sorted. Then, these individual lists are merged recursively to make up a sorted array. 
#### Runtime
O(N * log(N))

### QuickSort
#### Algorithm
This algorithm is also a recursive divide and conquer algorithm. This algorithm relies on the clever selection of the "pivot" point. The algorithm is as follows. First, a pivot point is selected. Then, this point is swapped with the last element in the array. Then, the first value larger than the pivot point from the left of the array is determined. The first value smaller than the pivot point from the pivot point moving left is also determined. These items are swapped. If the index of the item from the left is greater than the index of the item from the right, the pivot and the item from the left are swapped. Quick sort is then called on the unsorted arrays to the left and right. 

The elements to the left of the array are now all less than the pivot point and the elements to the right are all greater.

 
#### Runtime
Worst case: O(N^2)
Average case with a proper pviot: O(N * log(N))
