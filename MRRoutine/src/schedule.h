#ifndef _SCHEDULE_H_
#define _SCHEDULE_H_
#include <iostream>
#include <string>
#include <vector>
using namespace std; 

#include "login.h"

struct Task 
{
    int id; 
    string taskName;
    string startTime; 
    int duration;  
};

void getTasks(User usr , vector <Task> & tasks);
void scheduleTasks(vector<Task> & tasks);
void printTasks(const vector<Task> &tasks);

#endif