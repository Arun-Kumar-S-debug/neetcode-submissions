class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        j=list(allowed)
        count=0
        for i in words:
            m=True
            for k in i:
                if k in j:
                    continue
                m=False
                break
            if m:
                count+=1
        return count 