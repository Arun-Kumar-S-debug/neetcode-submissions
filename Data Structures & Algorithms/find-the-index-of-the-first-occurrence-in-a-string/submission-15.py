class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=0
        h=0
        while h<len(haystack):
            if needle[n]==haystack[h]:
                n+=1
                if n==len(needle):
                    return h-len(needle)+1
            else:
                h-=n-1
                n=0
                continue
            h+=1
        return -1