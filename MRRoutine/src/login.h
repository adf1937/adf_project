#ifndef _LOGIN_H_
#define _LOGIN_H_

#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

struct User
{
    string name;
    string status;
};

vector<string> getUserName(const string &FILE_WAY);

void newUserName(const string &NAME_FILE_WAY, const string &STATUS_FILE_WAY, const string &USER_FILE_WAY, User user);

User login();

bool rebuild();

#endif
