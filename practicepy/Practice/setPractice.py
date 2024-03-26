num=[1,1,2,3,4,5]
print(set(num))

s="ninu"
print(s[1])
t=''.join(sorted(s))
print(t)
print("##########")
hm={"ninu":1,"mary":3}
print(hm.get(s[1]))

print("##########")
def isAnagram(s: str, t):
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1+countS.get(s[i],1)
        print(countS.get(s[i], 0))
        countT[t[i]] = 1+countT.get(t[i], 0)
        print("333##########")
        print(countS.get(s[i],7))
        print("444##########")
        print(countT)

    return countS == countT

isAnagram("ninu","unin")