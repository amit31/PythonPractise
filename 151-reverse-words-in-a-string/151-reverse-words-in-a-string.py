class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip(" ")
       
        k=s.split(" ")
        print(k)
        ans=[]
        fans=""
       
        for i in range(len(k)-1,-1,-1):
            print(k[i])
            if k[i]=="":
                i=i+1
            else:
                k[i]=k[i]+" "
                ans.append(k[i])
        
        fans="".join(ans)
        size=len(fans)-1
       
        
        return fans[0:size]