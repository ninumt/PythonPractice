from collections import Counter
class Solution:
    def isAnagram(self, s:str, t:str)->bool:
        #return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False
        hashMapS, hashMapT = {},{}
        for i in range(len(s)):
            hashMapS[s[i]]=1+hashMapS.get(s[i],0)
            hashMapT[s[i]]=1+hashMapT.get(s[i],0)
        for c in hashMapS:
            if hashMapS[c] != hashMapT.get(c,0):
                return False
        return True

print(Solution().isAnagram("ninu","unin"))
print(Solution().isAnagram("ninu","unin"))







