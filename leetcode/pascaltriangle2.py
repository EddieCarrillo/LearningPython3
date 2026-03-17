class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        last = [1,1]
        lastIdx = 1
        while (lastIdx < rowIndex):
            latestPasc = [1]
            buildIdx = 1
            while buildIdx <= lastIdx:
                latestPasc.append(last[buildIdx] + last[buildIdx - 1])
                buildIdx += 1
            latestPasc.append(1)
            #Now we have a new row, which will be the new last one
            lastIdx += 1
            last = latestPasc
        return last
