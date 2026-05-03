class Solution(object):
    def divisorSubstrings(self, num, k):
        s = str(num)
        count = 0
        
        for i in range(len(s) - k + 1):
            sub = int(s[i:i+k])
            
            if sub != 0 and num % sub == 0:
                count += 1
                
        return count