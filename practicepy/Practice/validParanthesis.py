def valid_Paranthesis(s):
    stack=[]
    hashM={')':'(', '}':'{', ']':'['}
    for i in s:
        if i in hashM:
            if stack and stack[-1] == hashM[i]:
                stack.pop()
        else:
            stack.append(i)

    if not stack:
        return True
    else:
        return False


    # or --> return True if not stack else False

def validPara(s):#wrong
        stack=[]
        c=0
        for i in s:
            if i=='(':
                stack.append(i)
                continue
            if i==')':
                if not stack:
                    c+=1
                else:
                    if stack[-1]=='(':
                        stack.pop()
                continue
            c+=1
        return True if not stack else False

def validPar(s):#wrong
    stack = []
    i = 0
    parentheses = {')':'(', '}':'{', ']':'['}
    while i < len(s):
        if stack and stack[-1] == parentheses.get(s[i], None):
            stack.pop()
        else:
            stack.append(s[i])
        i += 1
    return True if not stack else False

print(validPar('()(){{{'))
print(validPara('()(){{{'))
print(validPara('()[]{}}'))
print(valid_Paranthesis('()(){{{'))
print(valid_Paranthesis('()[]{}'))
print(valid_Paranthesis('((('))
print(valid_Paranthesis(')))'))#wrong result
print(valid_Paranthesis(')}]'))#wrong result
print(valid_Paranthesis('[(){}[]]'))

