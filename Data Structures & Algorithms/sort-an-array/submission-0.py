class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)-1):
            min_index=i
            for j in range(i+1,len(nums)):
                if nums[min_index]>nums[j]:
                    min_index=j
            swap_value=nums[i]
            nums[i]=nums[min_index]
            nums[min_index]=swap_value
        return (nums)