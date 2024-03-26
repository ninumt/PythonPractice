"""Print a pyramid of this pattern
    *
   * *
  * * *
 * * * *
* * * * *

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

*
**
***
****
*****

* * * * *
* * * *
* * *
* *
*

     1
    12
   1212
  121212
 12121212
1212121212

*
* *
* * *
* * * *
* * * * *

* * * * *
* * * *
* * *
* *
*





"""

def pyramid1(rows):
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ", end="")
        for j in range(i+1):
            print("*", end=" ")
        print()

def pyramid2(rows):
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()

def pyramid3(rows):
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print()

def pyramid4(rows):
    for i in range(rows):
        for j in range(i+1):
            print("*",end="")
        print()

def pyramid5(rows):
    for i in range(rows):
        for j in range(rows-i):
            print("* ", end="")
        print()

def printNoPyramid6(rows):
    print(" "*5,end="1")
    print()
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ",end="")
        for j in range(i+1):
            print("1",end="2")
        print()

def increasingPyramid(rows):
    for i in range(rows):
        for j in range(i+1):
            print("* ", end="")
        print()

def decreasingPyramid(rows):
    for i in range(rows):
        for j in range(i,rows):
            print("* ", end="")
        print()

def pyramidWithSpace6(rows):
    for i in range(rows):
        for j in range(2*rows-i):
            print(" ",end="")
        for j in range(2*rows):
            print("*",end=" ")
        print()




"""    
     1
    12
   1212
  121212
 12121212
1212121212

"""

"""       
          * * * * * * * * * * 
         * * * * * * * * * * 
        * * * * * * * * * * 
       * * * * * * * * * * 
      * * * * * * * * * * 
      
"""

pyramid1(5)
print()
pyramid2(5)
print()
pyramid3(5)
print()
pyramid4(5)
print()
pyramid5(5)
print()
printNoPyramid6(5)
print()
increasingPyramid(5)
print()
decreasingPyramid(5)


