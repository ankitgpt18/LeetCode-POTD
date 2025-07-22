class Solution:
    def maximumUniqueSubarray(self, nums):
        l = 0
        r = 0
        n = len(nums)
        freq = {}
        total = 0
        max_sum = 0

        while r < n:
            freq[nums[r]] = freq.get(nums[r], 0) + 1
            total += nums[r]

            while (r - l + 1) > len(freq):
                freq[nums[l]] -= 1
                total -= nums[l]
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1

            max_sum = max(max_sum, total)
            r += 1

        return max_sum
