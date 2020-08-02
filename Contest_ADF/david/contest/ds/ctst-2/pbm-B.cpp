#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    bool ngt = false;
    int first = 0;
    long long n = 0;

    cin >> s;

    if (s[0] == '-')
    {
        first = 1;
        printf("-");
    }

    int a = 0;
    for (int i = first; i < s.size(); i++)
    {
        n += (s[i] - '0') * pow(10, a);
        a++;
    }

    printf("%lld", n);

    return 0;
}