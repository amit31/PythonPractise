
class Solution:
    
    
    def isEquals(self,li,char):
        
        if li=="(" and char==")":
            return True
        if li=="{" and char=="}":
            return True
        if li=="[" and char=="]":
            return True
        else:
            return False
        
    
    def isValid(self, s: str) -> bool:
        st=[]
        for char in s:
            if len(st)!=0:
                li=st[-1]
                if self.isEquals(li,char):
                    st.pop()
                    continue
            st.append(char)
        return len(st)==0


