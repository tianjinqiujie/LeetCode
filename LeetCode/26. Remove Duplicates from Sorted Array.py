class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        L = 1
        for R in range(1, len(nums)):
            if nums[L-1] != nums[R]:
                nums[L] = nums[R]
                L += 1
        return L