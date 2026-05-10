class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1=[]
        for i in s:
            if i not in s1:
                s1.append(i)
        t1=[]
        for i in t:
            if i not in t1:
                t1.append(i)
        if len(s1)!=len(t1):
            return False
        for i in range(len(s1)):
            s=s.replace(s1[i],t1[i])
        return s==t