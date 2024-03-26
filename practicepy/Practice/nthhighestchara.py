def highestchar(word):
    hashMap={}
    for i in word.split(','):
        if i in hashMap:
            hashMap[i]=hashMap[i]+1
        else:
            hashMap[i]=1
    print(hashMap)
    for j in hashMap:
        if hashMap[j]==2:
            return j
        elif hashMap[j]!=2:
            return 0





print(highestchar("ninu,robin,jayden,aiden,ninu,jayden,jayden,robin,robin,ninu,ninu"))
print(highestchar("n,n,b,f,g,h,j,k,b,b,f"))
l="10,11,10,12,13"
print(highestchar((l)))