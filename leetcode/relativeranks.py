from typing import List
class Solution:
        def findRelativeRanks(self, scores: List[int]) -> List[str]:

                sorted_ranks = sorted(scores, reverse=True)
                relative_ranks = {}
                for i in range(0, len(sorted_ranks)):
                        if i == 0:
                                relative_ranks[sorted_ranks[i]] = "Gold Medal"
                        elif i == 1:
                                relative_ranks[sorted_ranks[i]] = "Silver Medal"
                        elif i == 2:
                                relative_ranks[sorted_ranks[i]] = "Bronze Medal"
                        else:
                                relative_ranks[sorted_ranks[i]] = f"{i+1}"
                return [relative_ranks[score] for score in scores]


sol = Solution()
print(sol.findRelativeRanks([5,4,3,2,1]))
