class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l=heights.copy()
        l.sort()
        order=0
        for i,k in zip(heights,l):
            if i!=k:
                order+=1
        return order