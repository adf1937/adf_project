#include <bits/stdc++.h>
using namespace std;

vector<int> stk;

int max()
{
    int maxN = 0;

    for (int i = 0; i < stk.size(); i++)
    {
        if (stk[i] > maxN)
        {
            maxN = stk[i];
        }
    }

    return maxN;
}

int main()
{
    int oprN = 0;
    int n = 0;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> oprN;
        if (oprN == 0)
        {
            int pushN = 0;
            cin >> pushN;

            stk.push_back(pushN);
        }
        else if (oprN == 1)
        {
            if (stk.size() != 0)
            {
                stk.pop_back();
            }
        }
        else if (oprN == 2)
        {
            cout << max() << endl;
        }
        else
        {
            continue;
        }
    }

    return 0;
}