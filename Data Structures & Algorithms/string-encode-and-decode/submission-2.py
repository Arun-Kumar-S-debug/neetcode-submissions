class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s=s+"அ"+i
        return s
    def decode(self, s: str) -> List[str]:
        strs=[]
        start=0
        for i in range(0,len(s)):
            if s[i]=="அ":
                strs.append(s[start:i])
                start=i+1
        strs.append(s[start:len(s)])
        strs.remove("")
        return (strs)