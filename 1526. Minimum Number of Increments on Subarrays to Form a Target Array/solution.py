class Solution:
    def minNumberOperations(self, target):
        total = target[0]
        for i in range(1, len(target)):
            total += max(target[i] - target[i - 1], 0)
        return total
