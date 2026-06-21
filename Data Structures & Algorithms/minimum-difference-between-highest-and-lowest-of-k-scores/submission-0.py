class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        nu=nums[0:k]
        mini=-1
        for i in range(1,len(nums)-k+2):
            if mini==-1:
                mini=max(nu)-min(nu)
            if mini>(max(nu)-min(nu)):
                mini=max(nu)-min(nu)
            nu=nums[i:k+i]
        return mini