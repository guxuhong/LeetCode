"""
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        def traverse(ans, node, height):
            if len(ans) <= height:
                ans.append(node.val)
            else:
                ans[height] = node.val
            if node.left:
                traverse(ans, node.left, height + 1)
            if node.right:
                traverse(ans, node.right, height + 1)
        ans = []
        traverse(ans, root, 0)
        return ans
 
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        queue = [root]
        ans = []
        while queue:
            size = len(queue)
            ans.append(queue[0].val)
            for i in range(size):
                temp = queue.pop(0)
                if temp.right:
                    queue.append(temp.right)
                if temp.left:
                    queue.append(temp.left)
        return ans
