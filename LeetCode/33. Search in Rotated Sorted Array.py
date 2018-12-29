class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index,num in enumerate(nums):
            if num == target:
                return index
        return -1


a = Solution().search([4,5,6,7,0,1,2],3)
print(a)