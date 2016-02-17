"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(node, total, ans):
            if total == sum and node.left == node.right == None:
                res.append(ans + [node.val])
            else:
                if node.left:
                    dfs(node.left, total + node.left.val, ans + [node.val])
                if node.right:
                    dfs(node.right, total + node.right.val, ans + [node.val])
        res = []
        if root:
            dfs(root, root.val, [])
        return res
