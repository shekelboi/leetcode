from typing import Optional
from TreeBase import *


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    return Tree.are_trees_equal(p, q)


tree1 = Tree()
tree1.root = TreeNode(1)
tree1.root.left = TreeNode(2)

tree2 = Tree()
tree2.root = TreeNode(1)
tree2.root.left = TreeNode(2)
tree2.root.right = TreeNode(None)

print(isSameTree(tree1.root, tree2.root))