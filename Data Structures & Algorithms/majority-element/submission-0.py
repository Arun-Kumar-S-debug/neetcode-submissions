class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums1=list(set(nums))
        count=0
        val=0
        for i in nums1:
            count1=0
            for j in nums:
                if i==j:
                    count1+=1
            if count<count1:
                count=count1
                val=i
        return val