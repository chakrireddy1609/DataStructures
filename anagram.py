class Anagram:
    def anag(self,s,t):
        if len(s) != len(t):
            print("Not an anagram")

        else:
            sCount, tCount = {}, {}
            for i in range(len(s)):
                sCount[s[i]] = 1+sCount.get(s[i],0)
                tCount[t[i]] = 1+tCount.get(t[i],0)
            for j in sCount:
                if sCount[j] != tCount.get(j,0):
                    print("Not an anagram")

            print("Anagram")


a = Anagram()
a.anag("anagram","aanrma")
