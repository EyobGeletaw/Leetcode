class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        mainprefix = strs[0]
        
        for i in range(1, len(strs)):
            j = 0
            prefix = ""
            
            while j < len(mainprefix) and j < len(strs[i]) and mainprefix[j] == strs[i][j]:
                prefix += mainprefix[j]
                j += 1
            
            mainprefix = prefix
            
            if mainprefix == "":
                return ""
        
        return mainprefix