class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        j=int(nums[0]%2)
        for i in range(1,len(nums),2):
            if int(nums[i]%2)==j:
                return False
            if int(nums[i-1]%2)==abs(1-j):
                return False
        return True