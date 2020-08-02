#include <bits/stdc++.h>
using namespace std;

int main()
{
    stack<int> stk;
    int n = 0;

    do
    {
        cin >> n;

        if (n != 0)
        {
            stk.push(n);
        }
    } while (n != 0);

    while(stk.size() != 0)
    {
        cout << stk.top() << " ";
        stk.pop();
    }
    cout << endl;

    return 0;
}