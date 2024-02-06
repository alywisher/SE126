#1D list + function review + sequential search

import csv 

#create empty lists
#from file
lName = []
fName = []
test1 = []
test2 = []
test3 = []

#to be created 
numAvg = []
letAvg = []

# ---- FUNCTIONS ----
def menu():

    print("---CLASS ACOUNT MENU---")
    print("1. Show all Students")
    print("2. Show Roaster only")
    print("3. Search for a Student")
    print("4. EXIT")

    choice = int(input("Enter your chooice [1-4]: "))
    
    #loop trap user if they dont follow directions
    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("**INVALID** Digits only [1-4]")
        choice = int(input("Enter your chooice [1-4]: "))
    return choice

def seqSearch(searchTerm):

    #searchTerm is local var name and only exist in this def block

    #initilize foundIndex variable
    foundIndex = "" #set is empty

    #SEQUENTIAL SEARCH - "in sequence" -> start @ the beggining (0) go to the end (len(listName))
    for i in range(0, len(lName)):

        #look at eatch value in a list to find what your looking for
        if lName[i] == searchTerm:
            foundIndex = i #store index
        return foundIndex




#----  FILE / CONNECTION / LIST POPULATION ----
with open("week5/demo/listPractice1.txt") as csvFile:
    file = csv.reader(csvFile)

    for rec in file:
        #apend
        lName.append(rec[0])
        fName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
# ---- Disconect ----
print(f"{'LAST':12} \t{'FIRST':12} \t{'TEST1':4} \t{'TEST2':4} \t{'TEST3':4} \t{'NUMAV':5} \t{'LETAV':5}")
print("--------------------------------------------------------------------------------------------------------")

# ---- POPULATING ADDID=TINAL LISTS - NUM AVG AND LET AVG ----
for i in range(0, len(fName)):
    avg = (test1[i] + test2[i] + test3[i]) / 3
    numAvg.append(avg)

    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    elif avg >= 70:
        letter = "C"
    elif avg >= 60:
        letter = "D"
    elif avg < 60:
        letter = "F"
    else:
        letter = "**ERROR @ I***" + str(i)

    letAvg.append(letter)


#test file by print
for i in range(0, len(lName)):
    print(f"{lName[i]:12} \t{fName[i]:12} \t{test1[i]:4} \t{test2[i]:4} \t{test3[i]:4} \t{numAvg[i]:5.1f} \t{letAvg[i]:5}")

# ---- Main Code ----
    
menuChoice = menu()

while menuChoice != 4: # 4 is the exit
    #determin what the user wants to do
    if menuChoice == 1:
        print("\n\t---show all file data---")
    elif menuChoice == 2:
        print("\n\t---Show class roaster---")
    else: #menu choice 3
        print("\n\t---Search for student---")

        search = input("Enter the LAST name you are looking for: ")

        found = seqSearch(search)

        if found != "":
            #display result to user
            print(f"{lName[found]:12} \t{fName[found]:12} \t{test1[found]:4} \t{test2[found]:4} \t{test3[found]:4} \t{numAvg[found]:5.1f} \t{letAvg[found]:5}")
        else:
            print(f"the student {search} could not be found")
    #give opertunity to see menu/reselect, or exit
    #breaking out of loop
    menuChoice = menu()

print("\n\n\tThanks for using the program, Goodbye!")
