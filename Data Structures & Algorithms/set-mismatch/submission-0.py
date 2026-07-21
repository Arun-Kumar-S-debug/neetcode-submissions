class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(1,len(nums)+1):
            if nums.count(i)>1:
                result.insert(0,i)
            if nums.count(i)==0:
                result.append(i)
        return result