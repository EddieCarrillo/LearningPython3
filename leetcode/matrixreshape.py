class Solution:
        def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
                if r * c != len(mat) * len(mat[0]):
                        return mat
                reshaped_mat = [[0 for x in range(c)] for x in range(r)]
                re_r = 0
                re_c = 0
                for row in mat:
                        for element in row:
                                reshaped_mat[re_r][re_c] = element
                                re_c += 1
                                re_r += re_c // c
                                re_c %= c
                return reshaped_mat
