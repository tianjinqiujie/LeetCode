class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        _nums = nums[::-1]
        idx = -1
        for i in range(1, len(_nums)):
            if _nums[i] < _nums[i - 1]:
                idx = i
                break
        if idx != -1:
            tmp_nums = _nums[:idx]
            to_swap = min([n for n in tmp_nums if n > _nums[idx]])  # min(tmp_nums)
            tmp_nums[tmp_nums.index(to_swap)] = _nums[idx]
            _nums[idx] = to_swap
            _nums[:idx] = tmp_nums[::-1]
            _nums = _nums[::-1]
        for i in range(len(nums)):
            nums[i] = _nums[i]