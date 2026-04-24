class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list1=list(set(nums))
        list_count=[]
        result=[]
        for i in list1:
            count=0
            v=[]
            for j in nums:
                if i==j:
                    count+=1
            v.append(i)
            v.append(count)
            list_count.append(v)
        list_count.sort(key=lambda x:x[1])
        list_count.reverse()
        for i in range(k):
            result.append(list_count[i][0])
        return result