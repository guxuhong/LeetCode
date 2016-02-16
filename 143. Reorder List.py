"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.
For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:
            #find middle
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow
            left = head
            right = mid.next
            mid.next = None
        
            #reverse right half
            pre = None
            while right:
                next = right.next
                right.next = pre
                pre = right
                right = next
            right = pre
        
            #merge left and right
            dummy = ListNode(0)
            while left or right:
                if left != None:
                    dummy.next = left
                    left = left.next
                    dummy = dummy.next
                if right != None:
                    dummy.next = right
                    right = right.next
                    dummy = dummy.next
