# Test Suite
def runAllTests(test_string):
    print("Test Results:")
    # (1) Each value must be separated by a single comma
    print("\tRow Format Test: " +  ("Passed" if testDataFormat(test_string, False, False) else "Failed Due to error shown above"))
    # (2) Must only contain numerical values
    print("\tNumerical Only Test: " +  ("Passed" if testDataFormat(test_string, True, False) else "Failed Due to error shown above"))
    # (3) Ignore empty lines
    print("\tNo blank lines Test: " + ("Passed" if testDataFormat(test_string, False, True) else "Failed Due to error shown above"))

    print("Output String:")
    print(test_string)
    return testDataFormat(test_string, False, False) \
           and testDataFormat(test_string, False, False) \
           and testDataFormat(test_string, False, False)


def testDataFormat(test_data, test_num=False, test_blank=False):
    for lineNum,line in enumerate(test_data):
        for curVal in line.split(','):
            curVal = curVal.strip()
            if isInt(curVal) or isFloat(curVal):
                continue

            elif (not test_num and 'EXT' in curVal) or (not test_blank and not curVal):
                continue
            else:
                print("\t\t" + str(lineNum) + ":" + line + "\t\t'" + curVal + "'")
                return False
    return True


def isInt(in_str):
    try:
        int(in_str)
        return True
    except:
        return False


def isFloat(in_str):
    try:
        float(in_str)
        return True
    except:
        return False