class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        max = float("inf")
        nums.sort()
        n = len(nums)
        for i,j in enumerate(nums[:-2]):
            if i > 0 and nums[i-1] == j:continue
            l,r = i + 1,n - 1
            while(l < r):
                sum3 = j + nums[l] + nums[r]
                if(abs(sum3 - target) < abs(max - target)):
                    max = sum3
                if sum3 > target:
                    r -= 1
                elif sum3 < target:
                    l += 1
                else:return target
        return max


a = Solution()
print(a.threeSumClosest([-1, 0, 1, 2, -1, -4],4))