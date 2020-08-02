#include <bits/stdc++.h>
using namespace std;

struct GoodWord
{
    string word;
    int goodPersent;
};

GoodWord goodWord[100000];

int main()
{
    string s;
    int n = 0, p = 0;

    cin >> n >> p;
    for (int i = 0; i < n; i++)
    {
        cin >> goodWord[i].word >> goodWord[i].goodPersent;
    }

    

    return 0;
}