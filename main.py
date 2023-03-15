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

    def __str__(self):
        return f"{self.subject} - {self.name} | {self.duedate}"


# class to hold information about a Date
class Date:

    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        return f"{self.month}/{self.day}/{self.year}"


# adds Task(s) to tasklist
def add():
    response = " "
    while not no.__contains__(response.lower()):
        name = input("Enter the name of the Task: ")
        subject = input("Enter the subject of the Task: ")
        month = input("Enter the month of the Task: ")
        day = input("Enter the day the Task is due: ")
        year = input("Enter the year the Task is due, press Enter if the year is this year: ")
        if year == '':
            year = datetime.datetime.now().strftime("%Y")
        duedate = Date(month, day, year)
        task = Task(name, subject, duedate.__str__() + "\n")
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


# returns a boolean value that is whether date1 comes before date2 in the Gregorian calendar
def isEarlier(date1, date2):
    if date2.year > date1.year:
        return True
    elif date2.year < date1.year:
        return False
    else:
        if date2.month > date1.month:
            return True
        elif date2.month < date1.month:
            return False
        else:
            if date2.day > date1.day:
                return True
            else:
                return False


# sorts tasks by due date in tasklist
def sortByDueDate():
    return


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
        month = x[x.index(' | ') + 3:x.index("/")]
        second = x.find("/", 3)
        day = x[x.index("/") + 1:second]
        year = x[second + 1:len(x)]
        task = Task(name, subject, x)
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
