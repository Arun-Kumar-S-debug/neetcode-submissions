class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num1=list(set(nums))
        k=[]
        for i in num1:
            j=[i,nums.count(i)]
            k.append(j)
        k.sort(key=lambda x:x[0],reverse=True)
        k.sort(key=lambda x:x[1])
        result=[]
        for i in k:
            for j in range(i[1]):
                result.append(i[0])
        return result