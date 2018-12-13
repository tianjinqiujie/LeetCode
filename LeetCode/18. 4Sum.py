#-*- coding:utf-8 -*-
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, n, nums, limit = [], len(nums), sorted(nums), target >> 2
        for i in range(n-3):
            if nums[i] > limit:  #limit 1
                break
            if i != 0 and nums[i] == nums[i-1]: #remove duplicate
                continue
            for j in range(n-1,i+2,-1):   #Reverse traversal
                if nums[j] < limit: # limit 2
                    break
                if j != n -1 and nums[j] == nums[j+1]: #remove duplicate
                    continue
                lo, hi, sum2 = i + 1, j - 1, nums[i] + nums[j]
                limit2 = (target - sum2) >> 1
                while lo < hi and nums[lo] <= limit2 and nums[hi] >= limit2: #limit 3
                    sum = sum2 + nums[lo] + nums[hi]
                    if sum == target:
                        res += (nums[i], nums[lo], nums[hi], nums[j]),
                        while lo < hi and nums[hi] == nums[hi-1]: #remove duplicate
                            hi -= 1
                        while lo < hi and nums[lo] == nums[lo+1]: #remove duplicate
                            lo += 1
                    lo += sum <= target
                    hi -= sum >= target
        return res


a = Solution()
b = a.fourSum([1,2,3,4,5,6,0,1,-1,-1,-2],3)
print(b)