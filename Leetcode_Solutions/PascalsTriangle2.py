'''Return the asked row of pascals triangle'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]

        for i in range(1,rowIndex+1):
            row = [1]
            prev = res[i-1]

            for j in range(1,i):
                row.append(prev[j]+prev[j-1])
            row.append(1)
            res.append(row)
        return res[rowIndex]