class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        st=list(blocks[:k-1])
        result=float('inf')
        for i in range(k-1,len(blocks)):
            st.append(blocks[i])
            n=st.count('W')
            st.pop(0)
            result=min(result,n)
        return result