class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        nums1=list(set(nums))
        nums1.sort()
        index=nums1.index(0)
        result=nums1[len(nums1)-1]+1
        for i in range(0,max(nums1)):
            if i!=nums1[index]:
                if i>=1:
                    return (i)
            index+=1
        return (result)