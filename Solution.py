# Interview - Coding Exam
#########################
# Using Python, implement code to read the hard coded file data
# Manipulate the data to create an CSV formatted file with the following criteria:
#   (1) Each value must be separated by a single comma
#   (2) Must only contain numerical values
#   (3) Ignore empty lines

from Tests import runAllTests, isFloat, isInt
import xlsxwriter


def formatData(in_data):
    outList = []
    for line in in_data:
        if line == '\n':
            continue

        curLine = ''
        for curVal in line.split(','):
            curVal = curVal.strip()
            if isInt(curVal) or isFloat(curVal):
                curLine += curVal + ','
        curLine = curLine[:-1]
        outList.append(curLine)

    return outList


with open('raw_data.txt', 'r') as inFile:
    outData = formatData(inFile.readlines())

if runAllTests(outData):
    outData = [line.split(',') for line in outData]
    colCount = len(max(outData, key=len))

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('outFile.xlsx')
    worksheet = workbook.add_worksheet()

    for row, line in enumerate(outData):
        newLine = line.copy()
        if len(line) < colCount:
            newLine.extend([0] * (colCount - len(line)))
        for col,  val in enumerate(newLine):
            worksheet.write(row, col, float(val))


    workbook.close()