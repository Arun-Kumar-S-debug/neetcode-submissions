class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result=[]
        for i in range(0,len(nums)-k+1):
            result.append(max(nums[i:k+i]))
        return result