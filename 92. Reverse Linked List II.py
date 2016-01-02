"""
Reverse a linked list from position m to n. Do it in-place and in one-pass. 
For example:
 Given 1->2->3->4->5->NULL, m = 2 and n = 4, 
 return 1->4->3->2->5->NULL. 
Note:
 Given m, n satisfy the following condition:
 1 ≤ m ≤ n ≤ length of list. 
"""

#我的渣渣代码
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        prex, start, i = None, head, 1
        while i < m:
            prex = start
            start = start.next
            i += 1
        end, subprex = start, None
        while i <= n:
            t = end.next
            end.next = subprex
            subprex = end
            end = t
            i += 1
        start.next = end
        if prex != None:
            prex.next = subprex
        else:
            head = subprex
        return head
        
#大神的代码
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prestart = dummy
        for i in range(m-1):
            prestart = prestart.next
        start = prestart.next
        for i in range(n-m):
            temp = prestart.next
            prestart.next = start.next
            start.next = start.next.next
            prestart.next.next = temp
        return dummy.next
