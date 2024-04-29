class reverseClass:
    '''
    comments: what is the class used for
    '''
    def __init__(self, startVal):
        '''
        this is the basic common  variables used in the class.
        '''
        self.start_value = startVal
    def addMethod(self,val1):
        '''

        :param val1:
        :return: start_value + val1
        '''
        return (self.start_value+val1)
    def substractmethod(self,val2):
        '''

        :param val2:
        :return: start value - val2
        '''
        return  (val2-self.start_value)
    def reverse(word):
        print("hi")
        return word[::-1]


if __name__=="__main__":
    inst1=reverseClass(20)
    addVVal=inst1.addMethod(20)
    subVal=inst1.substractmethod(10)
    print(f"return val of add {addVVal} \n,return val of sub is {subVal}")
    print(reverseClass.reverse("ninu robin"))