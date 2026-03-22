class Solution(object):
    def subsetXORSum(self, nums):
        total_or = 0
        
        for num in nums:
            total_or |= num
        
        return total_or * (1 << (len(nums) - 1))