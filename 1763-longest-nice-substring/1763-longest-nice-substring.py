class Solution(object):
    def longestNiceSubstring(self, s):
        if len(s) < 2:
            return ""

        chars = set(s)

        for i, c in enumerate(s):

            # if pair does not exist
            if c.lower() not in chars or c.upper() not in chars:

                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                if len(left) >= len(right):
                    return left
                else:
                    return right

        return s