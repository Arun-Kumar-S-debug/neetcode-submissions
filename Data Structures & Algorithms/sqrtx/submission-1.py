class Solution:
    def mySqrt(self, x: int) -> int:
        result=0
        l=1
        r=x
        while l<=r:
            m=(l+r)//2
            if x//m==m:
                return m
            elif x//m<m:
                result=m-1
                r=m-1
            else:
                l=m+1
        return result