def compact(word):
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

def compact_string(s):
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1

    result += s[-1] + str(count)
    return result

# Given string
print(compact_string("aaabbbccddee"))
print(compact("aabbccc"))