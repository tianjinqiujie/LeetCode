# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            first = curr
            second = curr.next

            # there is only one node left
            if not second:
                break

            third = second.next
            prev.next = second
            second.next = first
            first.next = third

            prev = curr
            curr = curr.next
        return dummy.next