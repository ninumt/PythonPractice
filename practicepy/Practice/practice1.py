def compact(word:str)->str:
    #aaabbcc
    count=1
    result=""
    for i in range(1,len(word)):
        if word[i] == word[i-1]:
            count+=1
        else:
            result += word[i-1] + str(count)
            count=1
    print(i)
    result+=word[-1]+str(count)

    return result

def compact1(word):
    i=0
    count=1
    newWord=""
    for i in range(1,len(word)):
            if word[i] == word[i-1]:
                count+=1
                #print(count)

            else:
                newWord+=word[i-1]+str(count)
                count=1
    newWord += word[-1] + str(count)
    return newWord

print(compact("abbc"))




