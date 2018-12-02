#-*- coding:utf-8 -*-
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        if num == num[::-1]:return True
        else:return False

a = Solution()
x = 12321
print(a.isPalindrome(x))