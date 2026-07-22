class Solution:
    def climbStairs(self, n: int) -> int:
        sereis=[1,1]
        k=2
        while n>=k:
            su=sum(sereis[len(sereis)-2:len(sereis)])
            sereis.append(su)
            k+=1
        return sereis[len(sereis)-1]
