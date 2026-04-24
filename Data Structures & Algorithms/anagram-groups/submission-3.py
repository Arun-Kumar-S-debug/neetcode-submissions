class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets=[[] for i in range(20)]
        lists=[]
        for i in strs:
            temp=sorted(i)
            if temp not in lists:
                lists.append(temp)
            index=lists.index(temp)
            bucket=buckets[index]
            bucket.append(i)
        return (buckets[:len(lists)])