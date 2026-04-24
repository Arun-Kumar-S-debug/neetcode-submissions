class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
            n=s[i].isalnum()
            while n==False and i<j:
                i+=1
                n=s[i].isalnum()
            n=s[j].isalnum()
            while n==False and i<j:
                j-=1
                n=s[j].isalnum()
            if s[i].isalnum() and s[j].isalnum():
                val1=s[i].lower()
                val2=s[j].lower()
                if val1==val2:
                    i+=1
                    j-=1
                    continue
                else:
                    return (False)
        return (True)
