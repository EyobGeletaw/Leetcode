class Solution(object):
    def dividePlayers(self, skill):
        if len(skill) % 2 != 0:
            return -1

        skill.sort()

        target = sum(skill) // (len(skill) // 2)

        left = 0
        right = len(skill) - 1
        mysum = 0

        while left < right:
            if skill[left] + skill[right] != target:
                return -1

            mysum += skill[left] * skill[right]
            left += 1
            right -= 1

        return mysum