#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

int main()
{
   char n[20];
   int reverse = 0;
   int remainder;
   int orignal;
   cout<<"Enter a word"<<endl;
   cin>>n;
   orignal = strlen(n);
   for (int i = 0;i<orignal;i++) //the code for comparing the characters of word on left and right
   {
       if(n[i] != n[orignal-i-1]) //comparing input
       {
           reverse = 1;
           break;
       }
   }

   //conditional result
   if (reverse)
   {
       cout<<n <<"is not a palindrome"<<endl;

   }
   else 
   cout<<n <<"is a palindrome"<<endl;
   return 0;
}