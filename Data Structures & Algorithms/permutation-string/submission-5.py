class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1=list(s1)
        set1.sort()
        set2=list(s2[0:len(s1)-1])
        l=0
        for i in range(len(s1)-1,len(s2)):
            set2.append(s2[i])
            set2.sort()
            if set1==set2:
                return True
            set2.remove(s2[l])
            l+=1
        return False