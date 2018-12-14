class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                top_element = stack.pop() if stack else 's'
                if mapping.get(ch) != top_element:
                    return False
        if stack:
            return False
        else:
            return True
s = '{(d)}'
a = Solution()
print(a.isValid(s))