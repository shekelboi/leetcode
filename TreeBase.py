from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The traversal algorithms seem to be correct
class Tree:
    def __init__(self, arr: List[int] = None):
        self.root = TreeNode()
        if arr is not None:
            self.__arr_to_tree(arr, self.root)

    # TODO: Review array to tree methods
    @staticmethod
    def arr_to_tree(arr):
        tree = Tree()
        tree.__arr_to_tree(arr, tree.root)
        return tree

    def __arr_to_tree(self, arr, node):
        if len(arr) == 0:
            return
        current = arr.pop(0)
        if current is not None:
            if node is not None:
                node.val = current
            else:
                node = TreeNode(current)
        else:
            return
        self.__arr_to_tree(arr, node.left)
        self.__arr_to_tree(arr, node.right)
        pass

    @staticmethod
    def in_order_traversal(node, arr: [int], ignore_none=True):
        if node is not None:
            Tree.in_order_traversal(node.left, arr)
            if not ignore_none or node.val is not None:
                arr.append(node.val)
            Tree.in_order_traversal(node.right, arr)

    def pre_order_traversal(self, node):
        self.__pre_order(node)
        print()

    def __pre_order(self, node, ignore_none=True):
        if node is not None:
            if not ignore_none or node.val is not None:
                print(node.val, end=" ")
            self.__pre_order(node.left)
            self.__pre_order(node.right)

    def post_order_traversal(self, node):
        self.__post_order(node)
        print()

    def __post_order(self, node, ignore_none=True):
        if node is not None:
            self.__post_order(node.left)
            self.__post_order(node.right)
            if not ignore_none or node.val is not None:
                print(node.val, end=" ")

# arr = [1, None, 2, 3]
# tree = Tree(arr)
# tree.in_order_traversal(tree.root)