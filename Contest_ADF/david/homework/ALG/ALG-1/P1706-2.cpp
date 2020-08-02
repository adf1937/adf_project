#include <bits/stdc++.h>
using namespace std;

int num[10];
bool b[10];
short gn = 0;

void fun(int step)
{
    if (step == gn)
    {
        for (int i = 0; i < gn; i++)
        {
            printf("%5d", num[i]);
        }
        printf("\n");

        return;
    }
    for (int i = 1; i <= gn; i++)
    {
        if (b[i] == true)
        {
            continue;
        }
        b[i] = true;

        num[step] = i;
        fun(step + 1);
        b[i] = false;
    }

    return;
}

int main()
{
    cin >> gn;

    fun(0);

    return 0;
}