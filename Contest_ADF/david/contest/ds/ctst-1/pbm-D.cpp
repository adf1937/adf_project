#include <bits/stdc++.h> //P1449
#include <cstdlib>
using namespace std;

int main()
{
    char *s[1024];
    char cstr[1024] = {0};
    char c[1024] = {0};
    stack<int> stk;
    bool end = false;

    scanf("%s", cstr);

    s[0] = strtok(cstr, "+-*/.@");
    int a = 0;

    while(s != NULL)
    {
        a++;
        s[a] = strtok(NULL, "+-*/.@");
    }

    while(s != NULL)
    {
        a++;
        s[a] = strtok(NULL, "0123456789.@");
    }

    /*

    while (!end)
    {
        s = strtok(NULL, ".@");

        int len = 0;

        len = strlen(s);

        if (s[len - 1] == '@')
        {
            end = true;
        }

        s[len - 1] = '\0';

        if ((s[i] != '+') || (s[i] != '-') || (s[i] != '*') || (s[i] != '/'))
        {
            stk.push(s[i] - '0');
            i++;
        }
        else
        {
            int a = 0, b = 0;

            a = stk.top();
            stk.pop();
            b = stk.top();
            stk.pop();

            if (s[i] == '+')
            {
                stk.push(b + a);
            }
            else if (s[i] == '-')
            {
                stk.push(b - a);
            }
            else if (s[i] == '*')
            {
                stk.push(b * a);
            }
            else if (s[i] == '/')
            {
                stk.push(b / a);
            }
            else
            {
                continue;
            }
        }
    }

    cout << stk.top() << endl;
    */

    return 0;
}