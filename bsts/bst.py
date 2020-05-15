import numpy as np
import math

class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def inorder(head):
    if head is None:
        return

    inorder(head.left)

    print(head.val)

    inorder(head.right)

def inorder_node(head):
    if head.left is None:
        if head.right is None:
            return head
        return inorder_node(head.right)
    return inorder_node(head.left)





def preorder(head):
    if head is None:
        return

    print(head.val)

    preorder(head.left)

    preorder(head.right)


def postorder(head):

    if head is None:
        return

    postorder(head.left)

    postorder(head.right)

    print(head.val)


def insert(node, val):
    if val > node.val:
        if node.right is None:
            node.right = Node(val)
            node.right.parent = node
        else:
            insert(node.right, val)
    else:
        if node.left is None:
            node.left = Node(val)
            node.left.parent = node
        else:
            insert(node.left, val)


def search(node, val):
    if node is None:
        return False
    elif val == node.val:
        return node
    elif val > node.val:
        return search(node.right, val)
    else:
        return search(node.left, val)


def delete(head, val):
    delete_node = search(head, val)
    if delete_node is True:
        if delete_node.left is None and delete_node.right is None:
            if delete_node.parent.left == delete_node:
                delete_node.parent.left = None
            else:
                delete_node.parent.right = None
        elif delete_node.left is None:
            if delete_node.parent.left == delete_node:
                delete_node.parent.left = delete_node.right
                delete_node.right.parent = delete_node.parent
            else:
                delete_node.parent.right = delete_node.right
                delete_node.
        else:



    node = inorder_node(head.right)


if __name__ == "__main__":
    base_array = [1, 5, 2, 1, 8, 3, 7, 3]

    head = Node(base_array.pop(0))

    for element in base_array:
        insert(head, element)

    print("\nIn Order Traversal:")
    inorder(head)

    print("\nPre-Order Traversal:")
    preorder(head)

    print("\nPost-Order Traversal:")
    postorder(head)


    simple_tree = [10, 5, 15]

    simple_tree_head = Node(simple_tree.pop(0))

    for element in simple_tree:
        insert(simple_tree_head, element)

