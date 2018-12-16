#-*- coding:utf-8 -*-

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        s = ""
        self.ParanthesisMaker(res, s, n, n)
        return res


    def ParanthesisMaker(self, res, s, n, m):
        if n > m:
            return
        if n == 0 and m == 0:
            res.append(s)
        if n > 0:
            temp = s + "("
            self.ParanthesisMaker(res, temp, n - 1, m)
        if m > 0:
            temp = s + ")"
            self.ParanthesisMaker(res, temp, n, m - 1)


a = Solution()
print(a.generateParenthesis(2))