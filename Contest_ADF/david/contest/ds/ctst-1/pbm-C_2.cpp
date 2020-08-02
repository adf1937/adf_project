// error
#include <bits/stdc++.h> // P2089
using namespace std;

int wgt[10] = {0};

void change(int n)
{
    int i = 0;

    while (n != 0 && i < 10)
    {
        wgt[i] = n % 3 + 1;
        n /= 3;
        i++;
    }
}

int main()
{
    const int MAXN = pow(3, 10);
    int n = 0;
    int way = 0;

    cin >> n;

    for (int i = 0; i < MAXN; i++)
    {
        change(i);

        if (wgt[0] + wgt[1]
          + wgt[2] + wgt[3]
          + wgt[4] + wgt[5]
          + wgt[6] + wgt[7]
          + wgt[8] + wgt[9] == n)
        {
            way++;
        }
    }

    cout << way << endl;

    for (int i = 0; i < MAXN; i++)
    {
        change(i);

        if (wgt[0] + wgt[1]
          + wgt[2] + wgt[3]
          + wgt[4] + wgt[5]
          + wgt[6] + wgt[7]
          + wgt[8] + wgt[9] == n)
        {
            for (int i = 0; i < 10; i++)
            {
                cout << wgt[i] << " ";
            }
            cout << endl;
        }
    }

    return 0;
}