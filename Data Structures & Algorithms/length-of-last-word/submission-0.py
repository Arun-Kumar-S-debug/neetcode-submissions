class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        m=s.split(" ")
        l=[i for i in m]
        k=len(l)-1
        while l[k] in " ":
            k-=1
        return len(l[k])