#coding=utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val_sum = l1.val + l2.val
        list_node = ListNode(val_sum % 10)
        a = val_sum // 10
        node = list_node
        while True:
            try:
                l1 = l1.next
            except:
                pass
            try:
                l2 = l2.next
            except:
                pass
            if not l1 and not l2:
                break
            elif not l1:
                l1_val = 0
                l2_val = l2.val
            elif not l2:
                l2_val = 0
                l1_val = l1.val
            else:
                l1_val = l1.val
                l2_val = l2.val
            val_sum = l1_val + l2_val + a
            temp_node = ListNode(val_sum % 10)
            node.next = temp_node
            node = temp_node
            a = val_sum // 10
        if a != 0:
            node.next = ListNode(a)
        return list_node

l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))
test = Solution()
print test.addTwoNumbers(l1,l2).val