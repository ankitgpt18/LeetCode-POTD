class Solution(object):
    def minOperations(self, nums):
    
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n=len(nums)
        oc=nums.count(1)
        if oc:
            return n-oc
        r=float('inf')
        for i in range(n-1):
            g=nums[i]
            for j in range(i+1,n):
                g=gcd(g,nums[j])
                if g==1:
                    r=min(r,j-i)
                    break
        if r==float('inf'):
            return -1
        return r+n-1

    

            


        
