#include <iostream>
#include <vector>
#include <string>

using namespace std;

/*

A character in UTF-8 can be anywhere from 1 to 4 bytes long. 
The bytes are 8 bits long and are subject to the following rules:
 - For a 1-byte character, the first bit is a 0, followed by its unicode code.
 - For an n-byte character, the first n bits are all 1s and the n + 1 bit is 0. 
  This is followed by n - 1 bytes in which the 2 most significant bits
  (that is, the leftmost 2) are 10.
  
  
Given an array of integers representing the data, 
return true if it can be converted to a valid UTF-8 encoding, otherwise return false.
*/
bool solution(std::vector<int> stream) 
{
    return false
}


void testSolution(){
    if (solution(std::vector<int>{197, 130, 1}) != true) 
    {
        cout << "Failed 1" << endl;
    }
    if (solution(std::vector<int>{235, 140, 4}) != false) 
    {
        cout << "Failed 2" << endl;
    }
    if (solution(std::vector<int>{10}) != true) 
    {
        cout << "Failed 3" << endl;
    }
    if (solution(std::vector<int>{230, 136, 145}) != true) 
    {
        cout << "Failed 4" << endl;
    }
    if (solution(std::vector<int>{240, 162, 138, 147}) != true) 
    {
        cout << "Failed 5" << endl;
    }
    if (solution(std::vector<int>{255}) != false) 
    {
        cout << "Failed 6" << endl;
    }
    if (solution(std::vector<int>{240, 162, 138, 147, 17}) != true) 
    {
        cout << "Failed 7" << endl;
    }
    if (solution(std::vector<int>{237}) != false) 
    {
        cout << "Failed 8" << endl;
    }
    if (solution(std::vector<int>{145}) != false) 
    {
        cout << "Failed 9" << endl;
    }
    
    
}
int main()
{
    testSolution();
}
