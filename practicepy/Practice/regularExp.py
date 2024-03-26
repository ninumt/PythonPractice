import re

"""

. : Matches any single character except newline.
^ : Anchors the match at the start of the string.
$ : Anchors the match at the end of the string.
* : Matches zero or more occurrences of the preceding character.
+ : Matches one or more occurrences of the preceding character.
? : Matches zero or one occurrence of the preceding character.
[] : Specifies a character class (matches any one of the characters inside the brackets).
() : Creates a capturing group.
| : Acts like a logical OR.


eg:
\d matches any decimal digit.
+ is a quantifier that means "one or more occurrences".
So, r'\d+' will match one or more consecutive decimal digits in a string.

"""
my_list = ['123', '345', '55']
my_list_int = [int(x) for x in my_list]
print(min(my_list_int))
print(max(my_list_int))


s="abc123def345jk55"
ress=re.findall(r'\d+',s)
print(ress)
print(min(ress))

string1 = "cat, bat, rat, crt, caa, " \
         "caayy"# . Matches any single character except newline
matches1 = re.findall(r'c..', string1)
print(matches1)  # Output: ['cat', 'crt', 'caa', 'caa']

strings = ["app_app_les", "are", "redap", "but", "app_tenion", "isap", "apdif"]
matches = [string for string in strings if re.match(r'^ap', string)]
print(matches)


string2 = "apules banana cherry apples applesare"
matches2 = re.findall(r'ap..', string2)
print(matches2)#['apul', 'appl', 'appl']
print("############ 1")


fruitslist = string2.split(' ')#converts to list and split with space
print(type(fruitslist))
res= [fruit for fruit in fruitslist if re.match(r'^ap',fruit)]
result_string1 = ','.join(res)#apples,apples,applesare
result_string2 = ' '.join(res)#apples apples applesare
print(result_string1)
print(result_string2)