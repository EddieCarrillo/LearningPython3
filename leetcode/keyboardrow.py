class Solution:
   def findWords(self, words:List[str]) -> List[str]:
        row1_set = {'q','w','e','r','t','y','u','i','o','p'}
        row2_set = {'a','s','d','f','g','h','j','k','l'}
        row3_set = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        row_words = []

        for word in words:
            row1_points = 0
            row2_points = 0
            row3_points = 0
            for letter in word.lower():
                if letter in row1_set:
                    row1_points += 1
                if letter in row2_set:
                    row2_points += 1
                if letter in row3_set:
                    row3_points += 1
            if row2_points == 0 and row2_points == 0 and row1_points == len(word):
                row_words.append(word)
            if row1_points == 0 and row3_points == 0 and row2_points == len(word):
                row_words.append(word)
            if row1_points == 0 and row2_points == 0 and row3_points == len(word):
                row_words.append(word)
        return row_words

        
