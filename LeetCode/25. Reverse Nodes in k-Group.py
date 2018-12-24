# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # helper deque
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        deque = []
        while cur:
            deque.append(cur)
            cur = cur.next
            if len(deque) == k:
                while deque:
                    pre.next = deque.pop()
                    pre = pre.next
        # if total_len % k
        while deque:
            pre.next = deque.pop(0)
            pre = pre.next
        # tail must be None
        pre.next = None
        return dummy.next