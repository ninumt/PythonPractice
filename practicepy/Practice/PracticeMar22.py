import random

print([random.randint(0,99)])#[44] - prints only 1 value

print([random.randint(0,20) for _ in range(10)])
#print(l1) #[16, 17, 6, 9, 9, 7, 2, 1, 11, 18]
print("#############")

random.seed(2)
print([random.randint(0,99) for _ in range(10)])#[7, 11, 10, 46, 21, 94, 85, 39, 32, 77]
random.seed(2)
print([random.randint(0,99) for _ in range(20)])#[7, 11, 10, 46, 21, 94, 85, 39, 32, 77, 27, 77, 4, 74, 87, 20, 55, 81, 50, 92]
print("#############")

#print(random.shuffle(random.randint(0,99) for _ in range(10)))-->This returns None
print([_ for _ in range(0,20,2)]) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
l2=[i for i in range(0,10)]
print(l2)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(l2)
#print(random.shuffle(l2))#returns None so wrong,because the random.shuffle() function in Python shuffles the list in place and does not return anything (it returns None).
print(l2)#[3, 9, 1, 6, 0, 2, 4, 7, 5, 8]
print("#############")
##########SLICING##############
s="hello ninu"
#print(s[2:7])
print(s[-3:-1])#in
print(s[-3:])#inu
print(s[:-1])#hello nin
print(s[::-1])#unin olleh
print(s[1:3])#el

##########STRINGS##############
s1=" HellO JayDen   "
print(s1.upper())
print(s1.lower())
print(s1.strip())
print(s1.replace("JayD","Aid"))
print(s1.split(","))
s2="Aiden"
print(s1+s2)
s3=s1+s2
print(s3)


# from datetime import datetime
# print(datetime.now())#Give local time 2024-03-22 15:10:17.724736
# print(datetime.utcnow())#Gives UTC time 2024-03-22 19:10:17.724765
# deltatime= datetime.utcnow() - datetime.now()
# print(deltatime)# 3:59:59.999999
# print(type(deltatime))
#
#
# list1=[1,2,3,4,5,6]
# #print(list1)#[1,2,3,4,5,6]
# random.seed(2)
# random.shuffle(list1)
# print(list1)#Shuffles the list [4, 5, 2, 1, 3, 6]
#
# #random.seed(2)
# random.shuffle(list1)
# print(list1)#Shuffles the list [4, 5, 2, 1, 3, 6]
#
#
# print(random.random())#Random float no 0.6891226038269997
# print(random.random())
#
# print(random.randint(1,15))# random no between 1, 15 -->7
# print(random.random())
# print(random.random())
# print("*************")
#
#


