# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val,next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur_node = head
        for _ in range(n):
            cur_node = cur_node.next
        endN = head

        if cur_node == None:
            return head.next

        while cur_node.next != None:
            cur_node = cur_node.next
            endN = endN.next
        endN.next = endN.next.next
        return head

l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
a = Solution()
print((((a.removeNthFromEnd(l1,2).next).next).next).val)