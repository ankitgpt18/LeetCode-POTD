class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        ans=0
        width=[[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] !=0:
                    if j==0:
                        width[i][j]=1
                    else:
                        width[i][j]=width[i][j-1]+1

        for i in range(m):
            for j in range(n):
                minwidth=width[i][j]
                k=i
                while k>=0 and minwidth >0:
                    minwidth= min(minwidth,width[k][j])
                    ans=ans+minwidth
                    k=k-1
        return ans 



        
