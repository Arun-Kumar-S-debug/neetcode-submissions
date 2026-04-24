class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=[]
        nums1=list(set(nums))
        for i in nums1:
            count=0
            for j in nums:
                if i==j:
                    count+=1
            if count>(len(nums)//3):
                result.append(i)
        return result