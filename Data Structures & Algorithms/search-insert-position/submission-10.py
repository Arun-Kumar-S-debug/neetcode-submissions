class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result=len(nums)
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            print('low ',low,'  high ',high,'   mid ',mid)
            if nums[mid]==target:
                high=mid-1
                result=mid
            elif nums[mid]>target:
                high=mid-1
                result=mid
            else:
                low=mid+1
        return result