class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        k=['(','{','[']
        top=-1
        j=""
        if len(s)==1:
            return False
        for i in s:
            if i in k:
                st.append(i)
                top+=1
            elif top==-1:
                return False
            else:
                if i==']':
                    j='['
                elif i=='}':
                    j='{'
                else:
                    j='('
                if st[top]==j:
                    st.pop(top)
                    top-=1
                else:
                    return False
        if top==-1:
            return True
        else:
            return False