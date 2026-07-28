class Solution:
    def largestGoodInteger(self, num: str) -> str:
        k=[]
        count=0
        for i in range(len(num)-1):
            if num[i]==num[i+1]:
                count+=1
            else:
                count=0
            if count>1:
                k.append(int(num[i]))
        if len(k)>0:
            return str(max(k))*3
        return ""