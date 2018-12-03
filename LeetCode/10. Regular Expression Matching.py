#-*- coding:utf-8 -*-
import re
class Solution(object):
    def isMatch(self, s, p):
        memo = {}
        def dp(si, pi):
            if pi >= len(p): return si == len(s)
            if si >= len(s): return pi + 1 < len(p) and p[pi + 1] == '*' and dp(si, pi + 2)
            if (si, pi) not in memo:
                matched = p[pi] == '.' or p[pi] == s[si]
                if pi + 1 < len(p) and p[pi + 1] == '*':
                    memo[(si, pi)] = dp(si, pi + 2) or (matched and dp(si + 1, pi))
                else:
                    memo[(si, pi)] = matched and dp(si + 1, pi + 1)
            return memo[(si, pi)]
        return dp(0, 0)

a = Solution()
s = 'aa'
p = 'a'
print(a.isMatch(s,p))