class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s=s+"#|"+i
        return s
    def decode(self, s: str) -> List[str]:
        strs=[]
        start=2
        for i in range(0,len(s)-1):
            if s[i]=="#" and s[i+1]=="|":
                strs.append(s[start:i])
                start=i+2
        strs.append(s[start:len(s)])
        strs.remove("")
        return (strs)