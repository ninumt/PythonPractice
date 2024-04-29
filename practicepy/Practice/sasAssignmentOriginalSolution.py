# import re
# import logging
# from datetime import datetime
#
# logging.basicConfig(filename='../testLogs/myLogfile.log',
#                     level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')
# class dateTimeValidator:
#     '''
#     this class has methods to check
#     1.if the date is valid.
#     2.write valid date to output file
#     '''
#
#     # def checkDateValidity(self, dateString):
#     #     '''
#     #     checks if the date string is a valid UTC date format.
#     #     :param dateString:
#     #     :return: Date string if string is valid/ None if string is invalid.
#     #     '''
#     #
#     #     try:
#     #         dt = datetime.fromisoformat(dateString)
#     #         return dt
#     #     except ValueError:
#     #         return None
#
#
#     def checkDateValidity(self, dateString):
#         '''
#         checks if the date string is a valid UTC date format.
#         :param dateString:
#         :return: Date string if string is valid/ None if string is invalid.
#         '''
#         self.dateString = dateString
#         matchExpression = '^\d{4}-([0-1][0-2])-([0-2][0-9]|3[0-1])T([0-2][0-3]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9](Z|\+([0-2][0-3]|[0-1][0-9]):[0-5][0-9]|\-([0-2][0-3]|[0-1][0-9]):[0-5][0-9])$'
#
#         matchObj = re.search(matchExpression, self.dateString)
#         if matchObj:
#             logging.info(f"Valid date format {self.dateString} returning Date")
#             return self.dateString
#         else:
#             logging.info(f"Invalid date String {self.dateString} returning None ")
#             return None
#
# class dateClass(dateTimeValidator):
#     '''
#     this class handles input and output data files
#     '''
#     def __init__(self):
#         '''
#         Init method.
#         '''
#         self.inputFile = "../testData/input.txt"
#         self.outputFile = "../testOutput/output.txt"
#
#     def myFileReaderMethod(self):
#         '''
#
#         :param inputFile: input file path + file name
#         :return: list of lines in file
#         '''
#         self.inputFile = self.inputFile
#         with open(self.inputFile,'r') as fp:
#                 self.lines = fp.readlines()
#                 self.newlines = set()
#                 for line in self.lines:
#                     line= line.strip('\n')
#                     line = line.strip(',')
#                     line=line.strip()
#                     self.newlines.add(line)
#                 return list(self.newlines)
#
#
#     def myfileWriterMethod(self, validDateList):
#         '''
#         :param outputFile:
#         :return:
#         '''
#         self.validDateList = validDateList
#         with open(self.outputFile,'w') as fp:
#             for line in self.validDateList:
#                 fp.write(line + '\n')
#         return True
#
#     def findValidDate(self):
#         '''
#         find valid date from input file and write to an output file.
#         :return: True/False
#         '''
#         self.lines = self.myFileReaderMethod()
#         self.writeLines=[]
#         for line in self.lines:
#             status = self.checkDateValidity(line)
#             if status:
#                 print(f"About to write valid date {status} to file .")
#                 self.writeLines.append(status)
#             else:
#                 logging.info(f"Not writing date {line} as it is not a valid UTC date")
#                 continue
#
#         logging.info("writing to output file.")
#         self.myfileWriterMethod(self.writeLines)
#         print("Program Completed.")
#         return True
#
# if __name__=="__main__":
#     status = dateTimeValidator().findValidDate()
#
#
#
