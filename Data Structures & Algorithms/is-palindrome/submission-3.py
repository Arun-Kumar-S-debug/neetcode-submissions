class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
            n=bool(True*s[i].isalnum())
            while n==False:
                i+=1
                n=True
            n=bool(True*s[j].isalnum())
            while n==False:
                j-=1
                n=True
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
