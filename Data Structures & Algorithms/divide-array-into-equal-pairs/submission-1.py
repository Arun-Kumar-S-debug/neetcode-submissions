class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        k=list(set(nums))
        for i in k:
            j=nums.count(i)
            if j%2==1:
                return False
        return True