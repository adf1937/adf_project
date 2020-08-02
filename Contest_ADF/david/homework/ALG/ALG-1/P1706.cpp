#include <bits/stdc++.h>
using namespace std;

int num[10];
short gn = 0;

void fun(int n, int count)
{
    if (count == gn)
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
        bool dup = false;

        for (int j = 0; j < count; j++)
        {
            if (num[j] == i)
            {
                dup = true;
                break;
            }
        }
        if (dup == true)
        {
            continue;
        }

        num[count] = i;
        fun(i, count + 1);
    }

    return;
}

int main()
{
    cin >> gn;

    fun(0, 0);

    return 0;
}