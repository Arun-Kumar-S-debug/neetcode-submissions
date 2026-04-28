class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k=0
        j=0
        for i in nums:
            if i==1:
                j+=1
            else:
                k=max(k,j)
                j=0
        return max(k,j)