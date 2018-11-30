#coding=utf-8
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in nums:
#             other_num = target - i
#             if other_num in nums:
#                 if other_num != i:return [nums.index(i),nums.index(other_num)]
#                 else:
#                     iindex = nums.index(i)
#                     llist = nums[iindex+1:]
#                     if other_num in llist:
#                         return [iindex,llist.index(i)+iindex+1]
#         return('没有匹配的数字')

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            other_num = target - nums[i]
            if other_num in nums:
                if other_num != nums[i]:return [i,nums.index(other_num)]
                else:
                    llist = nums[i+1:]
                    if other_num in llist:
                        return [i,llist.index(other_num)+i+1]
        return('没有匹配的数字')

nums = [2, 3,5,7, 11, 15]
target = 10
twosum = Solution()
print twosum.twoSum(nums,target)
