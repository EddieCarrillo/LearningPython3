class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final_str = ""
        letter_idx = 0
        if len(strs) == 1:
            return strs[0]
        while True:
            mismatch = False
            for str_idx in range(1,len(strs)):
                if (len(strs[str_idx]) == 0):
                    mismatch = True
                    break
                if (letter_idx >= len(strs[str_idx]) or letter_idx >= len(strs[0])):
                    mismatch = True
                    break
                if (strs[str_idx][letter_idx] != strs[0][letter_idx]):
                    mismatch = True
                    break   
            if mismatch:
                break
            final_str = final_str + strs[0][letter_idx]
            letter_idx = letter_idx + 1   
        return final_str
            
