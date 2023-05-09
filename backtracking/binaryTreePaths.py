from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.paths = []
        # DFS
        self.traverse(root, [root.val])
        return self.paths
        
    def traverse(self, root, path) -> List[str]:
        # if leaf, record path
        if root.left is None and root.right is None:
            self.paths.append("->".join(list(map(str, path))))
        
        # go left and down to deepest
        if root.left:
            path.append(root.left.val)
            self.traverse(root.left, path)
            # backtrack
            path.pop()
        if root.right:
            path.append(root.right.val)
            self.traverse(root.right, path)
            # backtrack
            path.pop()
            
