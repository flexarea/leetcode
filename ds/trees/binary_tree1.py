class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def level_ord_traversal(res_arr, level, root):
    if root is None:
        return

    if len(res_arr) <= level:  # check if len of result array match current tree height
        res_arr.append([])  # create new entry for values at current level

    res_arr[level].append(root.data)
    # recursion
    level_ord_traversal(res_arr, level+1, root.left)
    level_ord_traversal(res_arr, level+1, root.right)


if __name__ == '__main__':
    # create new Node
    node = Node(10)
    node.left = Node(7)
    node.left.left = Node(5)
    node.left.right = Node(8)
    node.right = Node(12)
    node.right.right = Node(13)
    node.right.left = Node(11)

    res_arr = []  # final result should be 2D array

    level_ord_traversal(res_arr, 0, node)

    print(res_arr)
