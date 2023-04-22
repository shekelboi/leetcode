from typing import Optional
from TreeBase import *


def isSymmetric(root: Optional[TreeNode]) -> bool:
    return Tree.is_symmetric(root, root)


tree = Tree()
tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(2)
tree.root.left.right = TreeNode(3)
tree.root.right.right = TreeNode(3)

print(isSymmetric(tree.root))