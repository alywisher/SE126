#Allison Wisher
#1/31/2024
#Fourth Wing Dragon Data Base -> Midterm

#menu Function

#variable names: dragonName, namePronounce, nickName, meaning, color, type, riderFname, riderLname
#---- print colums ----
#print(f"{rec[0]:14}\t{rec[1]:16}\t{rec[2]:8}\t{rec[3]:14}\t{rec[4]:8}\t{rec[5]:14}\t{rec[6]:10}\t{rec[7]:14}")
#---- FUNCTION ----
def menu():

    print("\t\t\t| Dragon Encyclopedia Menu | ")
    print("\t\t\t1. Search By Dragon Name") #Show all info on Dragon
    print("\t\t\t2. Search By Rider Name") #show all info on dragon
    print("\t\t\t3. List Dragon Names") #Show only dragon names
    print("\t\t\t4. List Rider Names") #show only rider names
    print("\t\t\t5. EXIT")

    choice = int(input("Please Enter your Choice [1-5]: "))
    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        print("**ERROR** Please only enter digits [1-5] you halfwit")
        choice = int(input("Please Enter your Choice [1-5]: "))
    return choice

def dragonSearch(name):
     #searchTerm is local var name and only exist in this def block
    ids = search(name,dragonName)
    id = int(ids[0])
    print("---------------------------------------------------------------------------------------------------\n")
    print(f"{'DRAGON NAME':14} {'PRONOUNCIATION':16} {'NICK NAME':10} {'MEANING':14} {'COLOR':8} {'TYPE':14} {'RIDER FNAME':14} {'RIDER LNAME':10}")
    print(f"{dragonName[id]:14} {namePronounce[id]:16} {nickName[id]:10} {meaning[id]:14} {color[id]:8} {dragonType[id]:14} {riderFname[id]:10} {riderLname[id]:14}")
    input("")

def riderSearch(name, list):
     #searchTerm is local var name and only exist in this def block
    id = search(name,list)
    print(f"{dragonName[id]:14} {namePronounce[id]:16} {nickName[id]:8} {meaning[id]:14} {color[id]:8} {dragonType[id]:14} {riderFname[id]:10} {riderLname[id]:14}")
    return "" 
    
def search(identifier, list):
    #SEQUENTIAL SEARCH - "in sequence" -> start @ the beggining (0) go to the end (len(listName))
    ids = []
    for i in range(0, len(list)):
        #look at eatch value in a list to find what your looking for
        if list[i] == identifier:
            ids.append(i)
    return ids        

#---- MAIN CODE ----
dragonName = []
namePronounce = []
nickName = []
meaning = []
color = []
dragonType = [] 
riderFname = []
riderLname = []
#---- MAIN HEADER PRINT ----
import csv
with open("midtermIndividual/dragon.csv") as csvFile:
    #Reade from File
    
    file = csv.reader(csvFile)

    for rec in file:
        dragonName.append(rec[0])
        namePronounce.append(rec[1])
        nickName.append(rec[2])
        meaning.append(rec[3])
        color.append(rec[4])
        dragonType.append(rec[5])
        riderFname.append(rec[6])
        riderLname.append(rec[7])
      
#---- Disconect from csv ----
#header:
print("-------------------------------------------------------------------------------")
print("\t| Welcome to the Basgiath War College Dragon Encyclopedia |")
print("-------------------------------------------------------------------------------")

menuChoice = ""
while menuChoice != 5: # 5 is exit
    menuChoice = menu()
    if menuChoice == 1:
        name = input("Enter Dragon Name: ")
        dragonSearch(name)

    elif menuChoice == 2:
        
        choice = input("Would you like to search by [F]IRST or [L]AST name: ")
        while choice != "F" and choice != "L":
            print("**ERROR** Are you illiterate")
            choice = input("Would you like to search by [F]IRST or [L]AST name: ")

        name = input("Please Enter the name of the rider: ")
        if(choice == "F"):
            riderSearch(name, riderFname)
        else:
            riderSearch(name, riderLname)


    elif menuChoice == 3:
        print("---| Showing Dragon Names |---")
    elif menuChoice == 4:
        print("---| Showing Rider Names |---")
    


