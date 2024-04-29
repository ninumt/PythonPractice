import re
import logging



class dateTimeValidator:
    '''
    this class has methods to check
    1.if the date is valid.
    2.write valid date to output file

    '''
    def __init__(self):
        '''
        Init method .
        '''
        print("This is init method")

    def checkDateValidity(self,dateString):
        '''
        checks if the date string is a valid UTC date format.
        :param dateString:
        :return: Date string if string is valid/ None if string is invalid.
        '''
        self.dateStr = dateString
        #validator = '^\d{4}-([0-1][0-2])-([0-2][0-9]|3[0-1]T([0-2][0-3]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9](Z|\+([0-2][0-3]|[0-1][0-9]):[0-5][0-9]|\-([0-2][0-3]|[0-1][0-9]):[0-5][0-9]))$'
        validator = '^\d{4}-([0-1][0-2])-([0-2][0-9]|3[0-1])T([0-2][0-3]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9](Z|\+([0-2][0-3]|[0-1][0-9]):[0-5][0-9]|\-([0-2][0-3]|[0-1][0-9]):[0-5][0-9])$'

        matchObj = re.search(validator,self.dateStr)
        #import pdb;pdb.set_trace()
        if matchObj:
            print(f"Valid date format found for input date string {self.dateStr}")
            return self.dateStr
        else:
            # Logger.info(f"date String {self.dateStr}input for method is invalid UTC format, returning None ")
            return None

class dateHandler(dateTimeValidator):
    '''
    this class handles input and output data files
    '''
    def __init__(self):
        '''
        Init method.
        '''
        #self.defaultInputfile = "..practicepy/IOFiles/input.txt"
        self.defaultInputfile = "/Users/ninuthomas/NinuPython/NinuPython/PythonPractice/practicepy/IOFiles/input.txt"
        self.defaultOutfile = "/Users/ninuthomas/NinuPython/NinuPython/PythonPractice/practicepy/IOFiles/output.txt"
        with open(self.defaultOutfile,'w') as fp:
            fp.write('')
            print("Init the outout file")

    def myFileReaderMethod(self, inputFile=None):
        '''

        :param inputFile: input file path + file name
        :return: list of lines in file
        '''
        if inputFile==None:
            self.inputFile = self.defaultInputfile
        else:
            self.inputFile = inputFile

        try :
            with open(self.inputFile,'r') as fp:
                self.lines = list(set(fp.readlines()))
                return self.lines
        except Exception as e:
            print(f"Error opening the file {e}")
            return e

    def myfileWriterMethod(self,writeData,outputFile=None,):
        '''

        :param outputFile:
        :return:
        '''
        self.data =writeData
        if outputFile ==None:
            self.outputFile = self.defaultOutfile
        with open(self.outputFile,'a') as fp:
            fp.write(self.data)
            fp.write('\n')
            return True
        return False



    def findValidDate(self):
        '''
        find valid date from input file and write to an output file.
        :return: True/False
        '''
        self.lines = self.myFileReaderMethod()
        for line in self.lines:
            line = line.strip()
            line =line.strip(',')
            status = self.checkDateValidity(line)
            if status:
                print(f"About to write valid date {status} to file .")
                status = self.myfileWriterMethod(line)
                if status:
                    print(f"valid utc date  {line} written to file")
                else:
                    print(f"file write failed for valid date {line}")
                    return False
            else:
                # Logger.info(f"Not writing date {line} as it is not a valid UTC date")
                continue

        print("Program Completed.")
        return True

if __name__=="__main__":
    status=dateHandler().findValidDate()
    print (status)


