class Solution:
    def getRow(self,rowIndex):
        row=[1]
        for i in range(rowIndex):
            newRow=[1]
            for j in range(len(row)-1):
                newRow.append(row[j]+row[j+1])
            newRow.append(1) 
            row=newRow
        return row