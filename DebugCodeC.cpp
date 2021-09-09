/*
Expected output:
0  0  1  10  2  20  3  30  4  40
*/

#include <iostream>
using namespace std; 
void display(const Int constl=5)
{ 
   const int const2=5;
   int arrayl[constl]; 
   int array2[const2]; 
   for(int 1=0; i<5; 1++) 
  {  
     arrayl[i] = i; 
     array2[i] = i*10; 
     cout <<arrayl[i]<< ' ' << array2[i] << ' ' ; 
  }
} 
int main()
{ 
   display(5); 
   return 1;
}
