class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mini=-1
        for i in range(0,len(nums)-k+1):
            if mini==-1:
                mini=nums[i+k-1]-nums[i]
            else:
                mini=min(mini,nums[i+k-1]-nums[i])
        return mini