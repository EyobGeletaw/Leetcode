class Solution(object):
    def getDescentPeriods(self, prices):
        count = 1   # current streak
        ans = 1     # total (first element)
        
        for i in range(1, len(prices)):
            # check if descending by 1
            if prices[i] == prices[i - 1] - 1:
                count += 1   # extend streak
            else:
                count = 1    # reset
            
            ans += count     # add streak
        
        return ans