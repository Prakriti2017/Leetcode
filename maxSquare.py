class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        maxArea=0
        for i in range(row):
            for j in range(col):
                if(i==0 or j==0 and( matrix[i][j]=="1")):
                    maxArea=max(maxArea,1)
            
                elif(int(matrix[i][j])==1):
                    matrix[i][j]=min(int(matrix[i][j-1]),int(matrix[i-1][j]),int(matrix[i-1][j-1]))+1
                    maxArea=max(maxArea, matrix[i][j])  
                
                else:
                    continue
        return maxArea**2
    
s=Solution()
assert s.maximalSquare([["0"]])==0