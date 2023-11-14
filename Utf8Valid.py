"""
A character in UTF-8 can be anywhere from 1 to 4 bytes long. The bytes are 8 bits long and are subject to the
following rules:
    - For a 1 - byte character, the first bit is a 0, followed by its unicode code.
    - For an n - byte character, the first n bits are all 1s and the n + 1 bit is 0.
        This is followed by n - 1 bytes in which the 2 most significant bits (that is, the leftmost 2) are 10.

Given an array of integers representing the data, return true if it can be converted to a valid UTF-8
encoding, otherwise return false.
"""


def solution(in_arr: list[int]) -> bool:
    return False

TEST_CASES = [
    ([197, 130, 1], True),
    ([235, 140, 4], False),
    ([10], True),
    ([230, 136, 145], True),
    ([240, 162, 138, 147], True),
    ([255], False),
    ([240, 162, 138, 147, 17], True),
    ([237], False),
    ([145], False)
]
def testSolution():
    for caseNum,caseTuple in enumerate(TEST_CASES):
        if solution(caseTuple[0]) != caseTuple[1]:
            print(f'Failed test case #{str(caseNum)}')
        
        
if __name__ == '__main__':
    testSolution()
