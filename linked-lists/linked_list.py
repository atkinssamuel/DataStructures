class Node:
    def __init__(self, value):
        self.current_value = value
        self.next_node = None


if __name__ == "__main__":
    head = Node("Head")
    n1 = Node("Node 1")
    n2 = Node("Node 2")
    head.next_node = n1
    n1.next_node = n2

    current_node = head

    print("Printing Linked List:")
    while current_node is not None:
        print(current_node.current_value)
        current_node = current_node.next_node