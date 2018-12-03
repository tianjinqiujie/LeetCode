class Solution:
    # def maxArea(self, height):
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #     tmp = 0
    #     if not height:return 0
    #     for index1,value1 in enumerate(height):
    #         for index2,value2 in enumerate(height):
    #             if index1 == index2:break
    #             else:
    #                 value = abs(index1-index2)
    #                 cvalue = value*min(value1,value2)
    #                 if cvalue > tmp:tmp=cvalue
    #     return tmp
    def maxArea(self, height,result=0, L=0):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        R = len(height) - 1
        while L != R:
            result = max(result, min(height[L], height[R]) * (R - L))
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return result
a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))
