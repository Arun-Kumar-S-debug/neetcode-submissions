class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        for i in range(0,len(arr)-k+1):
            avg=sum(arr[i:i+k])/k
            if avg>=threshold:
                count+=1
        return count