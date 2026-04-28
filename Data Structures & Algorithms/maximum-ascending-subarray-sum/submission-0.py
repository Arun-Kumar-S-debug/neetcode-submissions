class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        j=[]
        k=0
        p=0
        for i in nums:
            if i>p:
                j.append(i)
                p=i
            else:
                k=max(k,sum(j))
                j.clear()
                j.append(i)
                p=i
        return max(k,sum(j))