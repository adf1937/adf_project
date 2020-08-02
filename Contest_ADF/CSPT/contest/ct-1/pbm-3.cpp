#include <bits/stdc++.h> //P1138
using namespace std;

bool cmp(int a, int b)
{
    return a > b;
}

int main()
{
    const int MAXN = 20000;
    int num[MAXN] = {0};
    int max = 0, n = 0;
    int lft = 0;

    cin >> max >> n;
    lft = max;
    for (int i = 0; i < n; i++)
    {
        cin >> num[i];
    }

    sort(num, num + n, cmp);

    int back = 0;
    /*while(num[back] < lft)
    {
        lft -= num[++back];
    }

    for (int i = back; i < n; i++)
    {
        if (num[i] < lft)
        {
            lft -= num[i];
        }
    }

    for (int i = (n - 1); i >= back; i--)
    {
        if (num[i] < lft)
        {
            lft -= num[i];
        }
    }*/

    for (int i = 0; i < n; i++)
    {
        if (num[i] > lft)
        {
            continue;
        }

        lft -= num[i];
    }

    cout << lft << endl;

    return 0;
}