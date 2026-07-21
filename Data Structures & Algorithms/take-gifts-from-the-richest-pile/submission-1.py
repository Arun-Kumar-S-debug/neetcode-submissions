import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            k=max(gifts)
            j=int(math.sqrt(k))
            gifts[gifts.index(k)]=j
        return sum(gifts)