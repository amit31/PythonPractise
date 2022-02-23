class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        map_m={}
        i=1
        total=0
        k=0
        for c in list(string.ascii_uppercase):
            map_m[c]=i
            i=i+1
     
        columnTitle=columnTitle[::-1]
        for j in range(len(columnTitle)):
            print(map_m.get(columnTitle[j]))
            total=total+map_m.get(columnTitle[j])*pow(26,k)
            k=k+1
                
                
        return total
        