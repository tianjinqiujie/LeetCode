class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0 ) :
            if dividend//divisor > 2**31-1:
                return 2**31-1
            return dividend//divisor
        else:
            if -(abs(dividend)//abs(divisor)) < -2**31:
                return -2**31
            return -(abs(dividend)//abs(divisor))

print(2**31-1)
a = Solution().divide(-2147483648,-1)
print(a)