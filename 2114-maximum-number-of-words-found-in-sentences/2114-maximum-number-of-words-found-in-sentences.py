class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        j=[]
        x=0
        ans=0
        #s_split=sentences.split(",")
        
        for i in sentences:
            j=i.split(" ")
            x=len(j)
            ans=max(x,ans)
        return ans
            
        