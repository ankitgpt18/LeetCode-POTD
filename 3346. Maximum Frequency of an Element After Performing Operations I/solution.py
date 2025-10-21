class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = max(nums)                  
        count = [0] * (n + 1)          
        for num in nums:
            count[num] += 1
        presum = [0]                   
        for i in range(n + 1):
            presum.append(presum[-1] + count[i])
        ans = 0
        for i in range(n + 1):
            left = presum[i] - presum[max(0, i-k)]            
            right = presum[min(n+1, i+k+1)] - presum[i+1]
            cur = count[i] + min(numOperations, left + right)   
            ans = max(ans, cur)                                 
        return ans
