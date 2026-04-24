class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        for i in nums:
            if i==val:
                count+=1
        for i in range(0,count):
            ind=nums.index(val)
            nums.pop(ind)
        return len(nums)