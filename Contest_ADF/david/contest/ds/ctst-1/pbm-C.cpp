#include <bits/stdc++.h>// P2089
using namespace std;

int main()
{
    int n = 0;
    int way = 0;
    int wgt[10] = {0};

    cin >> n;

    if ((n < 10) || (n > 30))
    {
        cout << 0 << endl;
        return 0;
    }

    for (int a = 1; a <= 3; a++)
    {
        wgt[0] = a;

        for (int b = 1; b <= 3; b++)
        {
            wgt[1] = b;

            for (int c = 1; c <= 3; c++)
            {
                wgt[2] = c;

                for (int d = 1; d <= 3; d++)
                {
                    wgt[3] = d;

                    for (int e = 1; e <= 3; e++)
                    {
                        wgt[4] = e;

                        for (int f = 1; f <= 3; f++)
                        {
                            wgt[5] = f;

                            for (int g = 1; g <= 3; g++)
                            {
                                wgt[6] = g;

                                for (int h = 1; h <= 3; h++)
                                {
                                    wgt[7] = h;

                                    for (int i = 1; i <= 3; i++)
                                    {
                                        wgt[8] = i;

                                        for (int j = 1; j <= 3; j++)
                                        {
                                            wgt[9] = j;

                                            if (wgt[0] + wgt[1]
                                              + wgt[2] + wgt[3]
                                              + wgt[4] + wgt[5]
                                              + wgt[6] + wgt[7]
                                              + wgt[8] + wgt[9] == n)
                                            {
                                                way++;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    cout << way << endl;

    for (int a = 1; a <= 3; a++)
    {
        wgt[0] = a;

        for (int b = 1; b <= 3; b++)
        {
            wgt[1] = b;

            for (int c = 1; c <= 3; c++)
            {
                wgt[2] = c;

                for (int d = 1; d <= 3; d++)
                {
                    wgt[3] = d;

                    for (int e = 1; e <= 3; e++)
                    {
                        wgt[4] = e;

                        for (int f = 1; f <= 3; f++)
                        {
                            wgt[5] = f;

                            for (int g = 1; g <= 3; g++)
                            {
                                wgt[6] = g;

                                for (int h = 1; h <= 3; h++)
                                {
                                    wgt[7] = h;

                                    for (int i = 1; i <= 3; i++)
                                    {
                                        wgt[8] = i;

                                        for (int j = 1; j <= 3; j++)
                                        {
                                            wgt[9] = j;

                                            if (wgt[0] + wgt[1]
                                              + wgt[2] + wgt[3]
                                              + wgt[4] + wgt[5]
                                              + wgt[6] + wgt[7]
                                              + wgt[8] + wgt[9] == n)
                                            {
                                                for (int i = 0; i < 10; i++)
                                                {
                                                    cout << wgt[i] << " ";
                                                }
                                                cout << endl;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    return 0;
}