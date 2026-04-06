class Solution(object):
    def reverseWords(self, s):
        words = s.split()        # Step 1: split into words
        words.reverse()         # Step 2: reverse list
        return " ".join(words)  # Step 3: join with single space