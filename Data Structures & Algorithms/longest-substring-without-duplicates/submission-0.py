class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        se=set()
        result=0
        for i in range(len(s)):
            while s[i] in se:
                se.remove(s[l])
                l+=1
            se.add(s[i])
            result=max(result,i-l+1)
        return result