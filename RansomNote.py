class Solution:

    def ransomNote(self,magazine,ransomnote):
        mdict = {}
        for i in magazine:
            if i in mdict:
                mdict[i] += 1
            else:
                mdict[i] = 1

        for j in ransomnote:
            if j not in mdict or mdict[j] == 0:
                return False
            else:
                mdict[j] -= 1
        return True


s = Solution()
print(s.ransomNote("abba","cb"))

