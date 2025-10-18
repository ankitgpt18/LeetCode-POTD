class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        cnt=0
        nums.sort()
        start=nums[0]-k
        for i in range(len(nums)):
            start=max(start,nums[i]-k)
            if nums[i]-k<=start<=nums[i]+k:
                cnt+=1
                start+=1
        return cnt
