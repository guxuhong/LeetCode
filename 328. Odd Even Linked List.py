"""
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
"""
#我的渣渣代码
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        end = head.next
        while end.next != None:
            end = end.next
        prex, current, stop = head, head.next, end
        while current != stop:
            end.next = current
            end = end.next
            prex.next = current.next
            if current.next == stop:
                end.next = None
                return head
            prex = prex.next
            current = prex.next
            end.next = None
        end.next = current
        end = end.next
        prex.next = current.next
        end.next = None
        return head

#大神的代码
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        old, even, evenhead = head, head.next, head.next
        while even and even.next:
            old.next = even.next
            old = old.next
            even.next = old.next
            even = even.next
        old.next = evenhead
        return head
