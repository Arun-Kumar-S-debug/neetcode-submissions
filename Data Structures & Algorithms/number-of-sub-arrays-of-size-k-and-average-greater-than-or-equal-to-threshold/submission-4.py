class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        tot=sum(arr[0:k])
        count=0
        if tot/k>=threshold:
                count+=1
        for i in range(0,len(arr)-k):
            tot=tot+arr[i+k]-arr[i]
            avg=tot/k
            if avg>=threshold:
                count+=1
        return count