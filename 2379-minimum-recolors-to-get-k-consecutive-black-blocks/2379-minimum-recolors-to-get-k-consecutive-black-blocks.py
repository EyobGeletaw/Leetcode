class Solution(object):
    def minimumRecolors(self, blocks, k):
        n = len(blocks)
        whites = 0
        
        # first window
        for i in range(k):
            if blocks[i] == 'W':
                whites += 1
        
        ans = whites
        
        # sliding window
        for i in range(k, n):
            if blocks[i - k] == 'W':
                whites -= 1
            if blocks[i] == 'W':
                whites += 1
            
            ans = min(ans, whites)
        
        return ans