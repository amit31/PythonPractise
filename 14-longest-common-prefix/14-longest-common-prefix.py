class Solution:
    def longestCommonPrefix( self,strs):
        
        if len(strs)==0 or strs[0]=="":
            return ""
        
        c=strs[0]
        mi=100
        for i in range(1,len(strs)):
            j = 0  
            k = 0
            ans = 0 
            while (j<len(c) and k < len(strs[i])):
                if c[j] == strs[i][k] : 
                    ans=ans+1
                else: 
                    break
                j=j+1
                k=k+1
            mi=min(mi,ans)
            print(mi)
        return c[0:mi]
        