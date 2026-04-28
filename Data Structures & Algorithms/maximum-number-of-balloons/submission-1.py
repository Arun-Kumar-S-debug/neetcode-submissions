class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        j=True
        c=list("balloon")
        text=list(text)
        count=0
        while j:
            for i in c:
                if i in text:
                    text.remove(i)
                else:
                    j=False
            count+=1
        return count-1