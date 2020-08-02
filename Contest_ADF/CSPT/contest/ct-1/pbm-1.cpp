#include <bits/stdc++.h> //P1138
using namespace std;

int main()
{
    const int N = 30010;
    int num[N] = {0};
    int n = 0, k = 0;

    cin >> n >> k;
    for (int i = 0; i < n; i++)
    {
        int j = 0;
        cin >> j;

        num[j]++;
    }

    int nu = 0;
    bool find = false;

    for (int i = 0; i < N; i++)
    {
        if (num[i] > 0)
        {
            nu++;
        }

        if (nu == k)
        {
            find = true;
            cout << i << endl;
            break;
        }
    }

    if (find == false)
    {
        cout << "NO RESULT" << endl;
    }

    return 0;
}