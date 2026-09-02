class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result=float('inf')
        sum1=0
        l=0
        for i in range(len(nums)):
            sum1+=nums[i]
            while sum1>=target:
                sum1-=nums[l]
                result=min(result,i-l+1)
                l+=1
        if result==float('inf'):
            return 0
        return result