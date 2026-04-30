class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        from collections import defaultdict
        
        freq = defaultdict(int)
        count = defaultdict(int)
        
        left = 0
        unique = 0
        res = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            if count[s[right]] == 1:
                unique += 1
            
            # keep window size = minSize
            if right - left + 1 > minSize:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    unique -= 1
                left += 1
            
            # check valid window
            if right - left + 1 == minSize and unique <= maxLetters:
                substring = s[left:right+1]
                freq[substring] += 1
                res = max(res, freq[substring])
        
        return res