class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        barry = []
        sarry = []
        for i in nums:
            if i >= 0:barry.append(i)
            else:sarry.append(i)