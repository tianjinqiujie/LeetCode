#-*- coding:utf-8 -*-
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if not digits:
            return []
        # initiate to the letters of first digit
        pre = dic[digits[0]]
        lst = []
        if len(digits) == 1:return [i for i in pre]
        for i in range(1, len(digits)):
            d = digits[i]
            curr = []
            for char in dic[d]:
                for e in pre:
                    # append one character to all ans before current digit is added
                    curr.append(e + char)
            pre = curr
        return pre

a = Solution()
b = a.letterCombinations('2')
print(b)