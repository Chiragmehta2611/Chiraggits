#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

//code for swapping
void swap(char *x ,char *y)
{
    char temp;
    temp = *x;
    *x = *y;
    *y = temp;
}    

//boolean for sorting the repeating characters
bool sorter(char str[] , int n , int m)
{
    for (int i = n ; i < m ; i++)
    if (str[i] == str [m])
    return 0;
    return 1;
}

//permutation
void permute(char *a, int l , int r)
{
    int i;
    if (l == r)
    {
    cout<< a <<endl;
    }

    else
    {
        for(i = l ; i <= r; i++)
        {   bool check = sorter(a , l, r); //checking the terms for repeating values
             if (check) 
            {
            swap( (a + l),(a + i));
            permute(a , l+1 , r);
            swap( (a + l),(a + i) );
            }
        }  
    }

}

//driver code
int main()
{
    char str[10];
    cout<<"Enter a string :"<<endl;
    cin>>str;
    int n = strlen(str);
    permute(str , 0 ,n-1);
    return 0;
}