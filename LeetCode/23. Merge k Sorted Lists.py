# from heapq import heappush, heappop, heapify
#
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
#
# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         # Add all list heads to heap.  Heap is list of tuples of (val, ListNode)
#         heap = [(node.val, node) for node in lists if node]
#         heapify(heap)
#
#         dummy = ListNode(None)  # dummy root. Actual root is dummy.next.
#         prev = dummy
#
#         while heap:
#             _, cur = heappop(heap)
#             if cur.next:
#                 heappush(heap, (cur.next.val, cur.next))
#             prev.next = cur
#             prev = cur
#
#         return dummy.next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def merge(node1, node2):
            l = ListNode(0)
            curr = l
            while True:
                if node1 is None:
                    curr.next = node2
                    break
                elif node2 is None:
                    curr.next = node1
                    break
                if node1.val <= node2.val:
                    curr.next = node1
                    curr = curr.next
                    node1 = node1.next
                else:
                    curr.next = node2
                    curr = curr.next
                    node2 = node2.next
            return l.next

        def dp(lists):
            n = len(lists)
            if n == 0:
                return lists
            elif n == 1:
                return lists[0]
            elif n == 2:
                return merge(lists[0], lists[1])
            else:
                return merge(dp(lists[:n // 2]), dp(lists[n // 2:]))

        return dp(lists)