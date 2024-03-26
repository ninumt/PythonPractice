

def goalParser(word):
    if not word:
        return 0
    i=0
    newWord=""
    while i < len(word):
        if word[i:i+2]=='()':
            newWord+='o'
            i+=2
        elif word[i]=="G":
            newWord+='C'
            i+=1
        elif word[i:i+4]=="(al)":
            newWord += "al"
            i+=4
        else:
            newWord +=word[i]
            i+=1
    return newWord

print(goalParser("()G() (al)GGGGG()(al)"))
print(goalParser("***)*[()G()(al)GGGGG()(al)]"))
"""def goalparserinter(word):

    Selenium=word.replace("()","o").replace("(al)","al").replace("G","C") # we are replacing 3 things 1.() --> o 2. (al)-->al 3. G-->C

    return Selenium

print(goalparserinter("G()(al)"))"""









