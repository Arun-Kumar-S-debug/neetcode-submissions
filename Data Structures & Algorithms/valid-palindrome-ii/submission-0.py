class Solution:
    def check(self,s):
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
    def validPalindrome(self, s: str) -> bool:
        k=self.check(s)
        if k==True:
            return True
        else:
            for i in range(len(s)):
                m=s[:i]+s[i+1:]
                k=self.check(m)
                if k==True:
                    return True
        return False
        