class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums1=list(set(nums))
        nums1.sort()
        if len(nums)==0:
            return 0
        count=1
        pre=0
        for i in range(0,len(nums1)-1):
            if nums1[i]==nums1[i+1]-1:
                count+=1
                continue
            else:
                if pre<count:
                    pre=count
                count=1
        if count<pre:
            count=pre
        return count