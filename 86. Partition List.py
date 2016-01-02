"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x. 
You should preserve the original relative order of the nodes in each of the two partitions. 
For example,
 Given 1->4->3->2->5->2 and x = 3,
 return 1->2->2->4->3->5. 
"""

#我的渣渣代码：
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None: return head
        start = dummy = ListNode(0)
        dummy.next = head
        while start.next != None and start.next.val < x:
            start = start.next
        if start.next != None:
            prex = start.next
            while prex.next != None:
                if prex.next.val < x:
                    t1 = start.next
                    start.next = prex.next
                    t2 = prex.next
                    prex.next = prex.next.next
                    t2.next = t1
                    start = start.next
                else:
                    prex = prex.next
        return dummy.next
        
#大神的代码：
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        headLess, headGreater = ListNode(0), ListNode(0)
        tLess, tGreater = headLess, headGreater
        temp = head
        while temp:
            if temp.val < x:
                tLess.next = temp
                temp = temp.next
                tLess = tLess.next
            else:
                tGreater.next = temp
                temp = temp.next
                tGreater = tGreater.next
                tGreater.next = None
        tLess.next = headGreater.next
        head = headLess.next
        return head
