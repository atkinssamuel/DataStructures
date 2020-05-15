### Binary Search Tress

```python
     1      # indices:         0
   -5 10    # indices:      1,   2
-11 -1 7 11 # indices:    3, 4, 5, 6
```

#### Element Access
Just as with other types of trees, we must define left, right, and parent indexing operations. Given that array indexing starts at 0, these functions are as follows:

```python
def get_left(index):
    return 2 * index + 1

def get_right(index):
    return 2 * index + 2

def get_parent(index):
    return math.floor((index-1)/2)
```


#### Functions
Basic BST Functions: Insert, Search, Delete

**These functions are implemented below:**
##### Search - Balanced = O(log(N)), Unbalanced = O(N)


##### Insert


##### Delete


#### Tree Traversal
By choosing the traversal of a tree in a clever way, one can accomplish specific goals. These traversal methods are detailed below:

##### Pre-Order
Pre-order traversal visits the root node first and then the left and the right nodes, respectively. It is called "pre-order" because the node is visited before (pre-) the left and right nodes.

##### Post-Order
This traversal type visits the left node, then the right node, then the parent node. This traversal type can be used to delete the tree. 

##### In-Order
The in order traversal visits the left node, then the parent node, then the right node. This traversal type is guaranteed to search the tree such that the elements are visited in ascending order. Reverse in-order traversal will search the nodes in descending order. 



