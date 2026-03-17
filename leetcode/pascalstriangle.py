class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        pascal = [[1],[1,1]]
        #row index
        row = 2
        while row < numRows:
            pascal.append([])
            #start with 1
            pascal[row].append(1)
            col = 1 #start at second element
            #must before the last element, which is always occupied by 1
            while col < row:
                pascal[row].append(pascal[row-1][col] + pascal[row-1][col-1])
                col += 1
            #end with 1
            pascal[row].append(1)
            row += 1
        return pascal
