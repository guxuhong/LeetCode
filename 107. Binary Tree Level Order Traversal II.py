"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).
For example:
 Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def subfunc(root, level, ans):
            if root:
                if len(ans) < level + 1:
                    ans.append([])
                ans[level].append(root.val)
                subfunc(root.left, level + 1, ans)
                subfunc(root.right, level + 1, ans)
        ans = []
        subfunc(root, 0, ans)
        ans.reverse()
        return ans
