# Rules:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.

# Definition for a binary tree node.
from asyncio.windows_events import NULL

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        t = TreeNode()

        # empty case
        if len(nums) == 0:
            return t
        
        # take the middle, repeat for left and right side
        return self.sortedArrayToBSTHelper(nums, t)
        
    def findMiddle(self, nums: list[int]) -> list[int]:
        # First middle element
        #int(len(list) / 2) - 1

        # Second middle element
        #int(len(list) / 2)
        
        # value of second middle element and its index
        return [nums[int(len(nums) / 2)], int(len(nums) / 2)]
    
    def sortedArrayToBSTHelper(self, nums: list[int], tree: TreeNode) -> TreeNode:
        
        tree.left = None
        tree.right = None
        
        if len(nums) <= 0:
            return tree
        
        # go through a list of int, recursively take the middle of the list, split left to recurse same operation, split right to curse same operation
        [middle, middleIndex] = self.findMiddle(nums)
        tree.val = middle
        
        # if node is end of ends, don't append anything
        if middleIndex <= 0 or middleIndex > len(nums) - 1:
            return tree
        
        # if left is not none, repeat
        if middleIndex > 0:
            tree.left = self.sortedArrayToBSTHelper(nums[:middleIndex], TreeNode())
        
        # if right is not none, repeat
        if middleIndex < len(nums) - 1:
            tree.right = self.sortedArrayToBSTHelper(nums[middleIndex+1:len(nums)], TreeNode())
        
        return tree

if __name__ == "__main__":
    s = Solution()
    t = TreeNode()
    testList = [
        [0],
        [-1],
        [-1, 0],
        [-1, 0, 1],
        [-1, -1, 0, 1],
        [-1, -1, 0, 1, 1],
        [3],
        [3, 7],
        [3, 7, 12],
        [3, 7, 12, 16],
        [3, 7, 12, 16, 22],
        [3, 7, 12, 16, 22, 24],
        [3, 7, 12, 16, 22, 24, 31],
        [-1, -1, 0, 1, 1, 3, 7, 12, 16, 22, 24, 31],
        [-10000, -1, 0, 1, 1, 3, 7, 12, 16, 22, 24, 31],
        [-10000, -1, 0, 1, 1, 3, 7, 12, 16, 22, 24, 10000],
    ]

    for test in testList:
        res = s.sortedArrayToBST(test)
        assert test == t.inorderTraversal(res)
        # print(test, t.inorderTraversal(res), True)
