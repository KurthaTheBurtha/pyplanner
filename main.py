# global variable which holds Task objects

global tasklist
tasklist=[]
# global variable which hold the possible inputs for a user stopping
global no
no=["no","n","","stop","break"]

# class to hold information about an assignment
class Task:
    def __init__(self, name, subject, duedate):
        self.name = name
        self.subject = subject
        self.duedate = duedate

    def __str__(self):
        return f"{self.subject} - {self.name} | {self.duedate}"


# adds Task(s) to tasklist
def add():
    response = " "
    while not no.__contains__(response.lower()):
        name = input("Enter the name of the Task: ")
        subject = input("Enter the subject of the Task: ")
        duedate = input("Enter the duedate of the Task: ")
        task = Task(name,subject,duedate+"\n")
        tasklist.append(task)
        response = input("Would you like to add another? y/n: ")


# removes Task(s) from tasklist
def remove():
    while True:
        printList()
        delete = input("Which task would you like to remove? Enter the number of the task that you want to remove, \"no\" or Enter to stop: ")
        if no.__contains__(delete):
            break
        tasklist.remove(tasklist[int(delete)-1])

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
        duedate = x[x.index(' | ') + 3:len(x)]
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
        print(str(count)+". "+tasklist[x].__str__(),end="")
        count+=1

# main code
readFile()
printList()
print()
# grab user input
response = input("What would you like to do? 1 - add a task | 2 - remove a task | 3 - view tasks | 4 - clear all tasks | Enter or stop to stop: ")
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
    response = input("Would you like to do anything else? 1 - add a task | 2 - remove a task | 3 - view tasks | 4 - clear all tasks | Enter or stop to stop: ")
    print()
writeFile()