# global variable which holds Task objects
import datetime

global tasklist
tasklist = []
# global variable which hold the possible inputs for a user stopping
global no
no = ["no", "n", "", "stop", "break"]


# class to hold information about an assignment
class Task:

    def __init__(self, name, subject, duedate):
        self.name = name
        self.subject = subject
        self.duedate = duedate

    def getdate(self):
        return self.duedate
    def __str__(self):
        date = self.duedate.strftime("%m/%d/%Y")
        return f"{self.subject} - {self.name} | {date}\n"


# adds Task(s) to tasklist
def add():
    response = " "
    while not no.__contains__(response.lower()):
        name = input("Enter the name of the Task: ")
        subject = input("Enter the subject of the Task: ")
        duedate = input("Enter the duedate of the Task: ")
        try:
            try:
                # tries to read input in YYYY/
                duedate = datetime.datetime(int(duedate[0:duedate.index('/')]),
                                            int(duedate[duedate.index('/') + 1:duedate.index('/', 5)]),
                                            int(duedate[duedate.index('/', 5) + 1:len(duedate)]))
            except:
                # defaults to current year if year isn't provided
                duedate = datetime.datetime(datetime.date.today().year, int(duedate[0:duedate.index('/')]),
                                            int(duedate[duedate.index('/') + 1:len(duedate)]))
        except:
            duedate = input("Improper format - Enter a date in format MM/DD or YYYY/MM/DD")
        task = Task(name, subject, duedate)
        tasklist.append(task)
        response = input("Would you like to add another? y/n: ")


# removes Task(s) from tasklist
def remove():
    while True:
        printList()
        delete = input(
            "Which task would you like to remove? Enter the number of the task that you want to remove, \"no\" or Enter to stop: ")
        if no.__contains__(delete):
            break
        tasklist.remove(tasklist[int(delete) - 1])


# sorts tasks by due date in tasklist
def sortTasks():
    quickSort(tasklist,0,len(tasklist))


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[high], array[i + 1])
    (array[i + 1], array[high]) = (array[high, array[i + 1]])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


# clears all tasks in tasklist
def clearTasks():
    file = open("assignments", "w")
    file.write("")
    tasklist.clear()
    print("Tasks cleared!")


# reads file "assignments" and processes it to tasklist
def readFile():
    file = open("assignments")
    for x in file:
        name = x[x.index(' - ') + 3:x.index(' | ')]
        subject = x[0:x.index(' - ')]
        duedate = x[x.index(' | ') + 3:len(x)]
        duedate = datetime.datetime(int(duedate[duedate.index('/', 5) + 1:len(duedate)]),
                                    int(duedate[0:duedate.index('/')]),
                                    int(duedate[duedate.index('/') + 1:duedate.index('/', 5)]))
        task = Task(name, subject, duedate)
        tasklist.append(task)


# writes tasklist to the file
def writeFile():
    file = open("assignments", "w")
    for x in tasklist:
        file.write(x.__str__())
    file.close()


# prints tasklist if not empty
def printList():
    count = 1
    for x in range(len(tasklist)):
        print(str(count) + ". " + tasklist[x].__str__(), end="")
        count += 1


# main code
readFile()
printList()
print()
# grab user input
response = input(
    "What would you like to do? 1 - add a task | 2 - remove a task | 3 - view tasks | 4 - clear all tasks | Enter or stop to stop: ")
while True:
    if no.__contains__(response.lower()):
        break
    elif response == "1":
        add()
    elif response == "2":
        remove()
    elif response == "3":
        printList()
    elif response == "4":
        clearTasks()
    else:
        response = input("Invalid response. Please try again: ")
    print()
    response = input(
        "Would you like to do anything else? 1 - add a task | 2 - remove a task | 3 - view tasks | 4 - clear all tasks | Enter or stop to stop: ")
    print()
writeFile()
