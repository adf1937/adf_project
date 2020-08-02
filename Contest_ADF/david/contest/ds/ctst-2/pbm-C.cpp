#include <bits/stdc++.h>
using namespace std;

int apr(int n, int x)
{
    int num[1000] = {0};
    int back = 0;
    int apn = 0;

    while (n != 0)
    {
        num[back] = n % 10;
        n /= 10;
        back++;
    }

    for (int i = 0; i < back; i++)
    {
        if (num[i] == x)
        {
            apn++;
        }
    }

    return apn;
}

int main()
{
    int n = 0, x = 0;
    int ti = 0;

    scanf("%d%d", &n, &x);

    for (int i = 1; i <= n; i++)
    {
        ti += apr(i, x);
    }

    printf("%d", ti);

    return 0;
}