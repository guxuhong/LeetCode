"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def sortedArrayToBST(array):
            length = len(array)
            if length == 0:
                return None
            res = TreeNode(array[length/2])
            res.left = sortedArrayToBST(array[:length/2])
            res.right = sortedArrayToBST(array[length/2 + 1:])
            return res
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return sortedArrayToBST(array)
