class Solution(object):
    def maxProduct(self, nums):
        max1 = float('-inf')   # largest
        max2 = float('-inf')   # second largest

        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

        return (max1 - 1) * (max2 - 1)