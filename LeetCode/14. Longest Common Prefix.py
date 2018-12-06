class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:return ""
        lenth = len(strs[0])
        for z in strs:
            if lenth > len(z):lenth = len(z)
        num = ''
        for i in range(lenth):
            dic = {}
            for j,k in enumerate(strs):
                dic[k[i]] = j
            if len(dic) == 1:num += strs[0][i]
            else:
                break
        return num
a = Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))
