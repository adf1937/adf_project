#include <bits/stdc++.h> //P2084
using namespace std;

int main()
{
    string s;
    int n[1000] = {0}, m = 0;

    cin >> m >> s;

    for (int i = 0; i < s.size(); i++)
    {
        n[i] = s[i] - '0';
    }

    printf("%d*%d^%d", n[0], m, (s.size() - 1));
    for (int i = 1; i < s.size(); i++)
    {
        if (n[i] != 0)
        {
            printf("+%d*%d^%d", n[i], m, (s.size() - 1 - i));
        }
    }

    return 0;
}