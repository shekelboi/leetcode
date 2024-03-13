from typing import List, Optional
from TreeBase import *


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    Tree.in_order_traversal(root, res)
    print(res)


tree = Tree()
tree.root = TreeNode(1)
tree.root.right = TreeNode(2)
tree.root.right.left = TreeNode(3)
print("Ok")
print(inorderTraversal(tree.root))