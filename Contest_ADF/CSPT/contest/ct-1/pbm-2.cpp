#include <bits/stdc++.h> //P1138
using namespace std;

struct Stu
{
    string nme; //name
    int tstAve; //test average
    int jgeAve; //judge average
    char ldr;   //leader
    char wst;   //west student
    int atc;    //article

    int rnk; //rank
    int mny; //money

    void get()
    {
        cin >> nme >> tstAve >> jgeAve >> ldr >> wst >> atc;
    }
    void money()
    {
        if ((tstAve > 80) && (atc > 0))
        {
            mny += 8000;
        }
        if ((tstAve > 85) && (jgeAve > 80))
        {
            mny += 4000;
        }
        if (tstAve > 90)
        {
            mny += 2000;
        }
        if ((tstAve > 85) && (wst == 'Y'))
        {
            mny += 1000;
        }
        if ((jgeAve > 80) && (ldr == 'Y'))
        {
            mny += 850;
        }
    }
};

bool cmp(Stu sa, Stu sb)
{
    if (sa.mny > sb.mny)
    {
        return true;
    }
    else if (sa.mny < sb.mny)
    {
        return false;
    }
    else
    {
        return sa.rnk < sb.rnk;
    }
}

const int MAXN = 100;
Stu stu[MAXN];

int main()
{
    int stuN = 0;
    int mnyAll = 0;

    cin >> stuN;
    for (int i = 0; i < stuN; i++)
    {
        stu[i].get();
        stu[i].rnk = (i + 1);
        stu[i].money();
    }

    for (int i = 0; i < stuN; i++)
    {
        mnyAll += stu[i].mny;
    }

    sort(stu, stu + stuN, cmp);

    cout << stu[0].nme << endl
         << stu[0].mny << endl;
    cout << mnyAll << endl;

    return 0;
}