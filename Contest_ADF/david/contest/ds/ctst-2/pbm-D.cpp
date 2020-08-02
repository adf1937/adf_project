#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;

ull power(ull x, ull y)
{
    ull n;

    for (int i = 0; i < y; i++)
    {
        n *= x;
    }

    return n;
}

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

int main()
{
    ull fab[50] = {0};
    int n = 0;
    int mod = 0;

    cin >> n;

    fab[0] = 1;
    fab[1] = 1;

    for (int i = 2; i < n; i++)
    {
        fab[i] = fab[i - 1] + fab[i - 2];
    }

    mod = fab[n - 1] % power(2, 31);

    cout << mod << "=";

    splt(mod);
    cout << endl;

    return 0;
}