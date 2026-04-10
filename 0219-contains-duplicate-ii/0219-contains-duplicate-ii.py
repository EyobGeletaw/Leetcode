class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        indexmap = {}

        for i, num in enumerate(nums):
            if num in indexmap and i - indexmap[num] <= k:
                return True

            indexmap[num] = i

        return False   