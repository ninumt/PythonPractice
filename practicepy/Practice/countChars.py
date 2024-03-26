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

def second_highest_character(string):
    character_count = {}

    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    print(character_count)

    #sorted_counts = sorted(character_count.items(), key=lambda x: x[1], reverse=True)#[('l', 4), ('h', 2), ('o', 2), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
    sorted_counts = sorted(character_count.items(), key=lambda x:x[1],reverse=True)
    print(sorted_counts)

    if len(sorted_counts) < 2:
        return None  # Not enough distinct characters

    second_highest_char = sorted_counts[1]
    return second_highest_char

# Example usage:
input_string = "hhelllo world"
result = second_highest_character(input_string)
print(result)







