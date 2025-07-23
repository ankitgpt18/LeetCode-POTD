class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
      
        if x < y:
            return self.remove(s, 'b', 'a', y, x) 
        else:
            return self.remove(s, 'a', 'b', x, y)  

    def remove(self, s: str, first: str, second: str, first_points: int, second_points: int) -> int:
        score = 0
        stack = []

        for ch in s:
            if stack and stack[-1] == first and ch == second:
                stack.pop()
                score += first_points
            else:
                stack.append(ch)

        final_stack = []
        for ch in stack:
            if final_stack and final_stack[-1] == second and ch == first:
                final_stack.pop()
                score += second_points
            else:
                final_stack.append(ch)

        return score
