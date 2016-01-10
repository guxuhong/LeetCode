"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if length == 0:
            return None
        ans = TreeNode(nums[length / 2])
        ans.left = self.sortedArrayToBST(nums[:length/2])
        ans.right = self.sortedArrayToBST(nums[length/2 + 1:])
        return ans
