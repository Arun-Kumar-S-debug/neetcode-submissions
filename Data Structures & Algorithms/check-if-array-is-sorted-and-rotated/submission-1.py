class Solution:
    def check(self, nums: List[int]) -> bool:
        j=min(nums)
        ind=nums.index(j)
        k=[]
        for i in range(len(nums)):
            ind=int(ind%len(nums))
            k.append(nums[ind])
            ind+=1
        nums.sort()
        return k==nums