class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        j=[]
        for i in grid:
            for k in i:
                j.append(k)
        j.sort()
        result=[]
        for i in range(len(j)):
            if i+1 not in j:
                result.append(i+1)
            if i+1<len(j):
                if j[i]-j[i+1]==0:
                    result.insert(0,j[i])
        return result