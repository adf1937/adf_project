#include <bits/stdc++.h> //P1059
using namespace std;

int main()
{
    const int N = 1010;
    int num[N] = {0};
    int sn[100] = {0};
    int n = 0;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int j = 0;
        cin >> j;

        num[j]++;
    }

    int ind = 0;
    for (int i = 0; i < N; i++)
    {
        if (num[i] > 0)
        {
            sn[ind] = i;
            ind++;
        }
    }

    sort(sn, sn + ind);

    cout << ind << endl;
    for (int i = 0; i < ind; i++)
    {
        cout << sn[i] << " ";
    }
    cout << endl;

    return 0;
}