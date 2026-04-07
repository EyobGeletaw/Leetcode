class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = set()
        left = 0
        max_len = 0
        # Expand the window using the right pointer
        for right in range(len(s)):
            while s[right] in window:  # If duplicate is found, shrink the window
                window.remove(s[left])  
                left += 1
            window.add(s[right])  # Add the new character to the window
            max_len = max(max_len, right - left + 1)
        
        return max_len
        
        