class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        set1=set()
        result=""
        for i in range(1,len(strs[0])+1):
            for j in strs:
                set1.add(j[0:i])
            if len(set1)==1:
                result=list(set1)[0]
            else:
                break
            set1.clear()
        return result