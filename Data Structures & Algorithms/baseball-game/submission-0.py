class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        score=0
        for i in operations:
            if i not in "+CD":
                st.append(int(i))
            elif i=="+":
                b=st.pop()
                a=st.pop()
                st.append(a)
                st.append(b)
                st.append(a+b)
            elif i=="C":
                st.pop()
            else:
                a=st.pop()
                st.append(a)
                st.append(a*2)
        for i in st:
            score+=i
        return score