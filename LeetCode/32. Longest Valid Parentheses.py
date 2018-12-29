class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        maxLen = 0
        for i,par in enumerate(s):
            if par=='(':
                stack.append(i)
            else:
                try:
                    stack.pop()
                    maxLen = max(maxLen, i-stack[-1])
                except:
                    stack.append(i)
        return maxLen

a = Solution().longestValidParentheses("()")
print(a)