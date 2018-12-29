class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index,num in enumerate(nums):
            if num >= target:return index
        return len(nums)


a = Solution().searchInsert([1,3,5,6],2)
print(a)