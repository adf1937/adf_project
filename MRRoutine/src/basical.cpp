
#include "basical.h"

string getCommand(const string ASKCODE)
{
    string command;

    cout << ASKCODE;
    getline(cin, command);

    return command;
}
