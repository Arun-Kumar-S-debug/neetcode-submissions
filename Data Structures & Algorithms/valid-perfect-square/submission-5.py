class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        r=num
        while l<=r:
            m=(l+r)//2
            if m==num/m:
                return True
            elif m>num/m:
                r=m-1
            else:
                l=m+1
        return False