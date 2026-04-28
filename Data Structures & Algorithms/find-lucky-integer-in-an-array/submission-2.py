class Solution:
    def findLucky(self, arr: List[int]) -> int:
        r=-1
        j=list(set(arr))
        for i in j:
            if arr.count(i)==i:
                r=max(r,i)
        return r