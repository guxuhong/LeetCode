"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity. 
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for list in lists:
            if list:
                heap.append((list.val, list))
        heapq.heapify(heap)
        head = curr = ListNode(0)
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next
