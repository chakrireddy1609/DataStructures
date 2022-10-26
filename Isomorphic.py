class Solution:

    def isomorphic(self,s,t):
        mapst, mapts = {},{}

        for c1,c2 in zip(s,t):
            if ((c1 in mapst and mapst[c1] != c2) or (c2 in mapts and mapts[c2] != c1)):
                return False

            mapst[c1] = c2
            mapts[c2] = c1
        return True

s = Solution()
print(s.isomorphic("egg","add"))
