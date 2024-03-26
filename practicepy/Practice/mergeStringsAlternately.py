def merge_alternate(word1, word2):
    merge=[]
    j = 0
    for i in word1:
        merge.append(i)
        for i in range(j,len(word2)):
            merge.append(word2[j])
            j+=1
            break
    if len(word2) > len(word1):
        remaining_words=word2[len(word1):]
        merge.append(remaining_words)
    #converting list to string
    converted_list = map(str, merge)
    result = ''.join(converted_list)
    return str(result)

def merge_alternate(word1, word2):
    merge=""
    for i in range(min(len(word1), len(word2))):
        merge+=word1[i]
        merge+=word2[i]
    if len(word1) > len(word2):
        remain=word1[len(word2):]
        merge+=remain
    else:
        remain = word2[len(word1):]
        merge += remain
    return merge


print(merge_alternate("abcdge","def"))
print(merge_alternate("abc","defghyi"))
print(merge_alternate("",""))
print(merge_alternate("","defghyi"))
print(merge_alternate("abcsss",""))












"""if len(word1) >= len(word2):
    longest_word = word1
    shortest_word = word2
else:
    longest_word = word2
    shortest_word = word1

print(longest_word)
print(shortest_word)"""
