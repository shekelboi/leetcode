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
    def in_order_traversal(node: TreeNode, arr: [int], ignore_none=True):
        if node is not None:
            Tree.in_order_traversal(node.left, arr, ignore_none)
            arr.append(node.val)
            Tree.in_order_traversal(node.right, arr, ignore_none)
        elif not ignore_none:
            arr.append(None)

    @staticmethod
    def pre_order_traversal(node: TreeNode, arr: [int], ignore_none=True):
        if node is not None:
            arr.append(node.val)
            Tree.pre_order_traversal(node.left, arr, ignore_none)
            Tree.pre_order_traversal(node.right, arr, ignore_none)
        elif not ignore_none:
            arr.append(None)

    @staticmethod
    def post_order_traversal(node: TreeNode, arr: [int], ignore_none=True):
        if node is not None:
            Tree.post_order_traversal(node.left, arr, ignore_none)
            Tree.post_order_traversal(node.right, arr, ignore_none)
            arr.append(node.val)
        elif not ignore_none:
            arr.append(None)

    @staticmethod
    def are_trees_equal(root1, root2):
        arr1 = []
        arr2 = []
        Tree.pre_order_traversal(root1, arr1, False)
        Tree.pre_order_traversal(root2, arr2, False)
        print(arr1)
        print(arr2)
        return arr1 == arr2

# arr = [1, None, 2, 3]
# tree = Tree(arr)
# tree.in_order_traversal(tree.root)