#allison Wisher
#lab 5 [individual] - 


#----FUNCTIONS----

def menu():

    print("--STUDENT SEARCH DATA BASE MENU--")
    print("1. Show All Student Report")
    print("2. Search for Student [ID]")
    print("3. Search for a student [Last]")
    print("4. view a Class Roster [class1, class2, class3]")
    print("5. EXIT")

    choice = int(input("Please enter your choice [1-5]: "))

    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        print("**INVALID CHOICE** Digits only [1-5]")
        choice= int(input("Please enter your choice [1-5] "))
    return choice 

#def seqSearch(searchTerm):

    #searchTerm is local var name and only exist in this def block

    #initilize foundIndex variable
    foundIndex = "" #set is empty

    #SEQUENTIAL SEARCH - "in sequence" -> start @ the beggining (0) go to the end (len(listName))
    for i in range(0, len(lName)):

        #look at eatch value in a list to find what your looking for
        if lName[i] == searchTerm:
            foundIndex = i #store index
        return foundIndex


#----CONNECT TO DOC----
import csv
#----MAIN CODE----

#----CREATING EMPTY LIST TO STORE DATA----
studID = []
lastName = []
firstName = []
class1 = []
class2 = []
class3 = []

#----CONNECTING AND READING FILE----
with open("week5/lab5_students.txt") as csvFile:

    for rec in csvFile:

        studID.append(rec[0])
        lastName.append(rec[1])
        firstName.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

#----DISCONECT FROM FILE----

print(f"{studID[i]}")

