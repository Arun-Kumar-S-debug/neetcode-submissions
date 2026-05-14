class Solution:
    def clearDigits(self, s: str) -> str:
        l=[]
        for i in s:
            if i in "1234567890":
                l.pop()
            else:
                l.append(i)
        result="".join(l)
        return result
