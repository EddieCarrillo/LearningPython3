from typing import List

class Solution:
        def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
                #this problem is about finding the overlap between the ranges,
                #then, printing out the size of the overlap.
                #suppose you have the ranges
                #[2,2], and [3,3]
                # well, [2,2] is going to be contained within [3,3]
                # so, it doesn't matter how many [3,3] we throw in the max
                # it [2,2] will always be contained in it
                # because the ops we get will always be from (0-m,0-n) this means
                # it will always start from the top left corner.
                # how about non-squares?
                #So, let's go with (2,2) and (1,3), so, we have
                # a 2x2 box for 2,2 and we have a 3 box top-row
                # what's the overlap, the first row,
                # so anything below that we disregard
                # so, one row,
                # but then, the third column is too much, it doesn't overlap with
                # the box
                # so we cut it down too
                # then we have (1,2) as our overlap
                # notice this is (min(2,1), min(2,3))
                # we claim this works generally, and will produce the overlap
                # and how about the number of elements in the overlap?
                # easy, just take the product, so, (min(2,1) * min(2,3))
                # this is our solution.
                overlap = (m,n)
                for op in ops:
                        overlap = (min(overlap[0], op[0]),min(overlap[1], op[1]))
                return overlap[0] * overlap[1]


sol = Solution()
print(sol.maxCount(3,3,[[2,2], [3,3]]))
print(sol.maxCount(3,3,[[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]))
print(sol.maxCount(3,3,[]))
