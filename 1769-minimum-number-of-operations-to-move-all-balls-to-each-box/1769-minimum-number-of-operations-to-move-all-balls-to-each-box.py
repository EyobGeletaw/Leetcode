class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        answer = [0] * n
        
        # Left to right
        balls = 0
        moves = 0
        for i in range(n):
            answer[i] += moves
            if boxes[i] == '1':
                balls += 1
            moves += balls
        
        # Right to left
        balls = 0
        moves = 0
        for i in range(n-1, -1, -1):
            answer[i] += moves
            if boxes[i] == '1':
                balls += 1
            moves += balls
        
        return answer