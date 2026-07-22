class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        n=len(mat)
        for i in range(0,n):
            sum+=mat[i][i]
            sum+=mat[n-i-1][i]
        if n%2==1:
            j=int(n/2)
            sum-=mat[j][j]
        return sum