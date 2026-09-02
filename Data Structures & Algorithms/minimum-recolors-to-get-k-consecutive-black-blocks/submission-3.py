class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        st=list(blocks[:k-1])
        result=float('inf')
        n=st.count('W')
        for i in range(k-1,len(blocks)):
            st.append(blocks[i])
            if blocks[i]=='W':
                n+=1
            result=min(result,n)
            if st[0]=='W':
                n-=1
            st.pop(0)
        return result