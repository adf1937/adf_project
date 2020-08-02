#include <bits/stdc++.h>
using namespace std; 

void splt(int n)
{
    int nu = 0;

    for (int i = 2; i  <= n; i++)
    {
        while (n % i == 0)
        {
            n /= i;

            nu++;
            if (nu > 1)
            {
                cout << "*";
            }

            cout << i;
        }

        if (n == 0)
        {
            break;
        }
    }
}


int main  ()
{
    int a ; 
    while(scanf("%d", &a) == 1)
    {
        splt(a);
    }
    return 0;
}