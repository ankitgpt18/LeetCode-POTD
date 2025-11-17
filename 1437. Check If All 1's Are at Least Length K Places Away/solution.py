class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_idx = None
        for idx,n in enumerate(nums):
            if n==1:
                if prev_idx is not None and idx-prev_idx-1<k:
                    return False
                prev_idx = idx
        return True


        
