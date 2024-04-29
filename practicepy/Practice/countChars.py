def countChar(s):
    HashM={}
    for char in s:
        if char in HashM:
            HashM[char]+=1
        else:
            HashM[char] = 1
    print(HashM)

    sortedKeys = sorted(HashM)
    print(sortedKeys)
    nhigh=0
    for r,t in sortedKeys.items():
        if t > nhigh:
            nhigh=t


    for i,j in HashM.items():
        if j==1:
            print(i)
            break

def n_highest_character(string, n ):
    character_count = {}

    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    print(character_count)#{'h': 2, 'e': 1, 'l': 4, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

    print(character_count.values());
    sorted_counts = sorted(character_count.items(), key=lambda x: x[1], reverse=True)#[('l', 4), ('h', 2), ('o', 2), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
    #Note ::: if x: x[1] sorts by  values, if x: x[1] , sorts by key if x: x[0]
    print(sorted_counts)

    if len(sorted_counts) < n:
        return None  # Not enough distinct characters

    second_highest_char = sorted_counts[n-1]#getting 2nd(nth) highest n-1
    return second_highest_char

# Example usage:
input_string = "hhelllo world"
result = n_highest_character(input_string,2)
print(result)







