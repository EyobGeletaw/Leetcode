class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        result = [0] * n
        
        # Case 1: k == 0
        if k == 0:
            return result
        
        # Case 2: k > 0
        if k > 0:
            for i in range(n):
                total = 0
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
                result[i] = total
        
        # Case 3: k < 0
        else:
            for i in range(n):
                total = 0
                for j in range(1, abs(k) + 1):
                    total += code[(i - j) % n]
                result[i] = total
        
        return result