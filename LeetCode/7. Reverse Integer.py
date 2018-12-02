#-*- coding:utf-8 -*-
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 2**31 -1 and x >= -2**31:
            strx = str(x)[::-1]
            if strx[-1] == '-':strx = '-' + strx[:-1]
            if int(strx) <= 2**31 -1 and int(strx) >= -2**31:return int(strx)
            else:return 0
        else:return 0


a = Solution()
x = 2147483648
print(a.reverse(x))