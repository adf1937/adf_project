#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    stack<char> stk;

    getline(cin, s, '@');

    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == '(')
        {
            stk.push(s[i]);
        }
        if (s[i] == ')')
        {
            if (stk.empty() != true)
            {
                stk.pop();
                continue;
            }

            printf("NO\n");
            return 0;
        }
    }

    if (stk.empty() == true)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }
    

    return 0;
}