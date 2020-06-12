#include "login.h"
#include "basical.h"
#include <fstream>
#include <cstdio>

using namespace std;


vector<string> getUserName(string FILE_WAY)
{
    vector<string> userName;

    ifstream fin_un(FILE_WAY); // User Name

    string s;
    while (std::getline(fin_un, s))
    {
        userName.push_back(s);
    }

    return userName;
};


void newUserName(const string NAME_FILE_WAY, const string STATUS_FILE_WAY, const string USER_FILE_WAY, User user)
{
    ofstream fout_un(NAME_FILE_WAY);   // User Name
    ofstream fout_us(STATUS_FILE_WAY); // User Status

    fout_un << user.name << std::endl;
    fout_us << user.status << std::endl;

    const string COMMAND = "mkdir -p " + USER_FILE_WAY;

    system(COMMAND.c_str());
};




User login() // unfinished
{
    User user;

    string STATUS_FILE_WAY;
    ofstream fout_usc(STATUS_FILE_WAY); // user_secret

    string logInStatus;
    cout << "   LOG IN" << endl
         << endl;

    logInStatus = getCommand("Log in or sign up?('log in' || 'sign up') : ");
    while ((logInStatus != "log in") && (logInStatus != "sign up"))
    {
        logInStatus = getCommand("Input error. Please input 'log in' or 'sign up' : ");
    }

    user.name = getCommand("Please input your User Name : ");

    /*vector<string> allName = getUserName
    if (logInStatus == "log in")
    {

    }*/

    return user;
}


