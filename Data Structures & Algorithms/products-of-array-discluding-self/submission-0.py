class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(0,len(nums)):
            value=1
            for j in range(0,len(nums)):
                if i==j:
                    continue
                else:
                    value=value*nums[j]
            result.append(value)
        return result