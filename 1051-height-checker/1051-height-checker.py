class Solution(object):
    def heightChecker(self, heights):
        count = [0] * 101
        
        for h in heights:
            count[h] += 1
        
        index = 0
        result = 0
        
        for height in range(1, 101):
            while count[height] > 0:
                if heights[index] != height:
                    result += 1
                index += 1
                count[height] -= 1
        
        return result