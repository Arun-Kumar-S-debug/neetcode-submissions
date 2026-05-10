class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            k=max(arr[i+1:len(arr)])
            arr[i]=k
        arr[len(arr)-1]=-1
        return arr