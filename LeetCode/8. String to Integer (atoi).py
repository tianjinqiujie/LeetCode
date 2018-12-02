#-*- coding:utf-8 -*-
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        value = ''
        str = str.strip()
        if str.startswith('+-') or str.startswith('++') or str.startswith('-+') or str.startswith('--'): return 0
        str = str.strip('+')
        if str.startswith('-'):
            value = '-'
            str = str.lstrip('-')
        for i in str:
            if i.isdigit():
                value += i
            else:
                try:
                    if int(value) >= 2**31 -1:return 2147483647
                    elif int(value) <= -2**31:return -2147483648
                    else:
                        return int(value)
                except:
                    return 0
        if value:
            try:
                if int(value) >= 2 ** 31 - 1:
                    return 2147483647
                elif int(value) <= -2 ** 31:
                    return -2147483648
                else:
                    return int(value)
            except:
                return 0
        return 0
a = Solution()
x = " ++1"
print(a.myAtoi(x))