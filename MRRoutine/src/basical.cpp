#include "basical.h"

string getCommand(bool return_string, const string &ASKCODE)
{
    string command;

    cout << ASKCODE;
    if (return_string)
    {
        getline(cin, command);
    }

    return command;
}