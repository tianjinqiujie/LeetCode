#-*- coding:utf-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s:
            maxStr = s[0]
            maxLen = 1
            resultLen = 0
            for t in s[1:]:
                if t in maxStr:
                    tempLen = len(maxStr)
                    if tempLen > maxLen:
                        maxLen = tempLen
                    maxStr += t
                    maxStr = maxStr[maxStr.index(t)+1:]
                else:
                    maxStr += t
                    resultLen = len(maxStr)
            return max(maxLen,resultLen)
        else:
            return 0
s = "nxuqinntxuqirq"
a = Solution()
print(a.lengthOfLongestSubstring(s))