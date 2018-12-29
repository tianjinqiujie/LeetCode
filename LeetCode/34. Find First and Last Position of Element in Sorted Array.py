class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        li = []
        for index,num in enumerate(nums):
            if num == target:
                li.append(index)
        if len(li) == 1:return li+li
        elif li == []:return [-1,-1]
        else:return [li[0],li[-1]]


a = Solution().searchRange([1,2,3,4,4,5,6],3)
print(a)