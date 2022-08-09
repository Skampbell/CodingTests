"""
Given an array a that contains only numbers in the range from 1 to in_arr.length,
find the first duplicate number for which the second occurrence has the minimal index.
In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a
smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example

For in_arr = [2, 1, 3, 5, 3, 2], the output should be getFirstDuplicate(in_arr) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

For in_arr = [2, 2], the output should be getFirstDuplicate(in_arr) = 2;

For in_arr = [2, 4, 3, 5, 1], the output should be getFirstDuplicate(in_arr) = -1.
"""

def getFirstDuplicate(in_arr):
    pass


def test():
    testArrs = [2, 1, 3, 5, 3, 2],[2, 2],[2, 4, 3, 5, 1],[1], [5, 5, 5, 5, 5]
    expected = [3, 2, -1, -1, 5]

    for arrNum,testArr in enumerate(testArrs):
        output = getFirstDuplicate(testArr)
        if output != expected[arrNum]:
            print('Failed input: ' + str(testArr))
            print('Expected = ' + str(expected[arrNum]) + ' != ' + str(output))
            return False

    print("Passed!")
    return True


test()
