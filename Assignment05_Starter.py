# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <JLi>,<08.08.2020>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "/Users/junleli/Documents/_PythonClass/assignment05/ToDoList.txt"
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
file = open(objFile, "r")
for row in file:
    strData = row.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
file.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        # TODO: Add Code Here
        print("Your Current Tasks Are:")
        for row in lstTable:
            print(row['Task'], ",", row['Priority'])
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        # TODO: Add Code Here
        strTask = input("Enter the Name of Your Task:")
        strPriority = input("Enter Your Task Priority[High or Low]:")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("New Task Added.")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        # TODO: Add Code Here
        strRemove = str(input("Enter Task to Remove:"))
        for row in lstTable:
            if row["Task"].lower() == strRemove.lower():
                lstTable.remove(row)
                print("Task", strRemove.upper(), "Removed.", sep=" ")
                break
            else:
                print("Please Enter the Correct Task Name.")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        # TODO: Add Code Here
        file = open(objFile, "w")
        for row in lstTable:
            file.write(row["Task"] + ", " + row["Priority"] + "\n")
        file.close()
        print("Data Saved!")
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        # TODO: Add Code Here
        print("Are You Sure to Exit the Program?")
        strExit = input("Enter [y] for yes, [n] for no:")
        if strExit == "y":
            print("Good Bye")
            break  # and Exit the program
        elif strExit == "n":
            continue  # continue the loop and back to start

    else:
        print("Please Enter 1, 2, 3, 4, and 5 Only.")
