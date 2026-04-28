class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        c1=1
        c2=1
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                c1+=1
            if nums[i]<=nums[i+1]:
                c2+=1
        if c1==len(nums) or c2==len(nums):
            return True
        else:
            return False