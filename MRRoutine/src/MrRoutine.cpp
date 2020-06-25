//============================================================================
// Name        : MrRoutine.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include "login.h"
#include "basical.h"
#include "schedule.h"
using namespace std;

int main() {
	User usr;
	usr = login();
	
	vector<Task> userTasks; 
	getTasks(usr, userTasks);
	scheduleTasks(userTasks);
	printTasks(userTasks);

	return 0;
}
