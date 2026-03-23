from typing import List

class Solution:
        def findContentChildren(self, g: List[int], s:List[int]) -> int:
                g.sort()
                s.sort()
                s_ptr = len(s) - 1
                g_ptr = len(g) - 1

                while s_ptr >= 0 and g_ptr >= 0:
                        cur_cookie = s[s_ptr]
                        cur_child = g[g_ptr]
                        if g[0] > cur_cookie:
                                break
                        #Cookies only get smaller from here
                        #so, don't even bother lookig.
                        if cur_cookie >= cur_child:
                                s_ptr -= 1
                                g_ptr -= 1
                        else:
                                g_ptr -= 1

                return len(s) - s_ptr - 1

g1 = [1,2,3]; s1 = [1,1]
g2 = [1,2]; s2 = [1,2,3]

sol = Solution()
print(sol.findContentChildren(g1,s1))
print(sol.findContentChildren(g2,s2))
