class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        dictd={}
        k=0

        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                 k=matrix[i][j]
                 dictd[k]=dictd.get(k,0)+1
        
        for key,value in dictd.items():
            if key == target:
                return True
        return False