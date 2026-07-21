class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if len(words[j])>=len(words[i]):
                    k=words[j]
                    if k[0:len(words[i])]==words[i] and k[len(words[j])-len(words[i]):]==words[i]:
                        count+=1
        return count