### Heap Guide:
Arrays that start with index 0 and arrays that start at index 1 must be treated differently in the context of heaps. Given that this is a Python implementation of heaps, array indexing starts at 0. 

#### Heap Traversal
Given an array [0, 23, 5, 1, 6, 2, 7], the heap looks like the following:
```Python
0               # indices:    0
23, 5           # indices:   1, 2 
1, 6, 2, 7      # indices: 3, 4, 5, 6
```
##### Left Child
To access the left child:
```Python
left_child_index = parent_index * 2 + 1
```

##### Right Child
To access the right child:
```Python
right_child_index = parent_index * 2 + 2
```
##### Parent
To access a parent index:
```Python
parent_index = floor((right_child_index - 1)/2) # Could also use left_child_index
```
#### Height
The height of the tree is:
```Python
height = math.ceil(math.log2(len(array) + 1) - 1)
```

### Heap Functions
#### Max Heapify
Max heapify looks at a particular node in the tree and propagates that node down the tree until it is greater than its children. The node in question is compared with its left and right children. If the left or right child is greater than the current node, the current node is swapped with the greater of the two. Then, max heapify is called at the location the node was swapped to. 
#### Create Max Heap
This function takes in an array and interchanges the elements until a max heap is formed. To do so, the function iterates over the parents of the leaves of the heap. For each parent, starting at the lowest, max heapify is called.
#### Insert
When inserting a new element, the new element is appended to the heap. Then, this element is compared with its parent. If it is greater than its parent it is swapped and then compared with its new parent. This process is repeated until the new element is less than its parent or it reaches the root. 
#### Extract
To extract an element, the root of the heap is swapped with the final element in the tree. Then, the new final element is popped off of the heap. To maintain the max heap, max heapify is called on the new root of the tree. This works because all of the other elements in the tree already obey the max heap property. 
