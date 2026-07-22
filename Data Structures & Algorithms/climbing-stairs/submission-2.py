class Solution:
    def climbStairs(self, n: int) -> int:
        ser=[1,1]
        k=2
        while n>=k:
            su=sum(ser[len(ser)-2:len(ser)])
            ser.append(su)
            k+=1
        return max(ser)
