class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0
        r=0
        while r<len(nums):
            if nums[r]>0:
                t=nums[r]
                nums[r]=nums[l]
                nums[l]=t
                l+=1
            r+=1
        return nums
        