class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result=[]
        l1=0
        l2=0
        while l1<len(nums) or l2<len(nums):
            j=True
            while j==True and l1<len(nums):
                if nums[l1]>0:
                    result.append(nums[l1])
                    j=False
                l1+=1
            j=True
            while j==True and l2<len(nums):
                if nums[l2]<0:
                    result.append(nums[l2])
                    j=False
                l2+=1
        return result