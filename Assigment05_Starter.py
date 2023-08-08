# ------------------------------------------------------------------------ #
# Title: Assignment05_Starter
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# Dev: RRoot, 1/1/2030, Created Script
# Date: August 5th, 2023
# Changelog: Eli Ritter, 8/5/2023, Edited Script
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# https://www.afterhoursprogramming.com/tutorial/python/reading-files/
#lstRow = []
#strFile = 'ToDoToDoList.txt'
#objFile = None

#objFile = open(strFile, "r")
#for row in objFile:
#    lstRow = row.split(",")
#    print(lstRow)
#    print(lstRow[0] + '|' + lstRow[1] + '|' + lstRow[2].strip())
#objFile.close()

#The code doesn't work when the above is implemented.

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data.
    2) Add a new item.
    3) Remove an existing item.
    4) Save data to file.
    5) Exit the program.
    """)
    strChoice = str(input("Which option would you like to perform? "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1' or strChoice.strip() == 'one' or strChoice.strip() == 'One'):
        print("Your current tasks are:")
        print(dicRow)


    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2' or strChoice.strip() == 'two' or strChoice.strip() == 'Two'):
        # Page one hundred and forty-five of the textbook.
        term = input("What task do you want me to add? ")
        if term not in dicRow:
            definition = input("What is the task's priority? ")
            dicRow[term] = definition
        else:
            print("That task already exists. Try redefining it.")
        lstTable += [dicRow]


    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3' or strChoice.strip() == 'three' or strChoice.strip() == 'Three'):
        # Page one hundred and forty-six of the textbook.
        term = input("What term do you want me to delete? ")
        if term in dicRow:
            del dicRow[term]
            print("Deleted.")
        else:
            print("Could not find term.")


    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4' or strChoice.strip() == 'four' or strChoice.strip() == 'Four'):
        objFile = open("ToDoToDoList.txt", "w")
        objFile.write(str(lstTable).strip())
        objFile.close()
        print("Data was saved.")


    # Step 7 - Exit program
    elif (strChoice.strip() == '5' or strChoice.strip() == 'five' or strChoice.strip() == 'Five'):
        break
    else:
        print("Please choose only one, two, three, four, or five.")