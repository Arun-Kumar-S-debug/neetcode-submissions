class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(0,len(nums)-1):
            value=nums[i]
            for j in range(i,len(nums)):
                if value>nums[i]:
                    value=nums[i]
            swap_value=nums[i]
            ind=nums.index(value)
            nums[i]=value
            nums[ind]=swap_value
        nums.sort()
        return nums
