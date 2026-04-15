class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        left = 0
        count = 0
        zero = 0
        one = 0

        for right in range(len(s)):
            # Add current character
            if s[right] == '0':
                zero += 1
            else:
                one += 1

            # Shrink window if BOTH exceed k (invalid case)
            while zero > k and one > k:
                if s[left] == '0':
                    zero -= 1
                else:
                    one -= 1
                left += 1

            # Count valid substrings ending at 'right'
            count += (right - left + 1)

        return count