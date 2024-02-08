#Allison Wisher
#1/31/2024
#Fourth Wing Dragon Data Base -> Midterm

#Variable Dicktionary:
# dragonName[rec(0)], namePronounce[rec(1)], nickName[rec(2)], meaning[rec(3)], dragonColor[rec(4)], dragonType[rec(5)], riderFname[rec(6)], riderLname[rec(7)] 

#---- FUNCTION ----
def menu():

    print("-------------------------------------------------------------------------------")
    print("\t| Welcome to the Basgiath War College Dragon Encyclopedia |")
    print("-------------------------------------------------------------------------------")

    print("\n\t\t\t| Dragon Encyclopedia Menu |\n")
    print("\t\t\t1. Search By Dragon Name") #Show all info on Dragon
    print("\t\t\t2. Search By Dragon Color") #Show all info on Dragon (via color search)
    print("\t\t\t3. Search By Dragon Type") #Show all info on Dragon (via type search)
    print("\t\t\t4. Search By Rider Name") #show all info on dragon
    print("\t\t\t5. List Dragon Names") #Show only dragon names
    print("\t\t\t6. List Rider Names") #show only rider names
    print("\t\t\t7. EXIT\n")

    choice = input("Please Enter your Choice [1-7]: ")
    while choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6' and choice != '7':
        print("**ERROR** Please only enter digits [1-7]")
        choice = input("Please Enter your Choice [1-7]: ")
    return int(choice) #stops code from breaking when enter is hit multiple times 

def dragonSearch(name):
     #searchTerm is local var name and only exist in this def block
    ids = search(name,dragonName)
    if ids == 0:
        print("**INVALID CONGRATS**") #ensure error doesnt break 
    else:
        print("----------------------------------------------------------------------------------------------------------------\n")
        print(f"{'DRAGON NAME':14} {'PRONOUNCIATION':16} {'NICK NAME':10} {'MEANING':14} {'COLOR':8} {'TYPE':14} {'RIDER FNAME':14} {'RIDER LNAME':10}")
        for id in ids:
            print(f"\t{dragonName[id]:14} {namePronounce[id]:16} {nickName[id]:10} {meaning[id]:14} {dragonColor[id]:8} {dragonType[id]:14} {riderFname[id]:14} {riderLname[id]:14}")
        
def dragonColorSearch(color): #add ability to find via color
     #searchTerm is local var name and only exist in this def block
    ids = search(color, dragonColor)
    if ids == 0:
        print("**INVALID CONGRATS**") #ensure error doesnt break 
    else:
        print("----------------------------------------------------------------------------------------------------------------\n")
        print(f"{'DRAGON NAME':14} {'PRONOUNCIATION':16} {'NICK NAME':10} {'MEANING':14} {'COLOR':8} {'TYPE':14} {'RIDER FNAME':14} {'RIDER LNAME':10}")
        for id in ids:
            print(f"{dragonName[id]:14} {namePronounce[id]:16} {nickName[id]:10} {meaning[id]:14} {dragonColor[id]:8} {dragonType[id]:14} {riderFname[id]:14} {riderLname[id]:14}")

def dragonTypeSearch(type): #add ability to find via type
     #searchTerm is local var name and only exist in this def block
    ids = search(type, dragonType)
    if ids == 0:
        print("**INVALID CONGRATS**") #ensure error doesnt break 
    else:
        print("----------------------------------------------------------------------------------------------------------------\n")
        print(f"{'DRAGON NAME':14} {'PRONOUNCIATION':16} {'NICK NAME':10} {'MEANING':14} {'COLOR':8} {'TYPE':14} {'RIDER FNAME':14} {'RIDER LNAME':10}")
        for id in ids:
            print(f"{dragonName[id]:14} {namePronounce[id]:16} {nickName[id]:10} {meaning[id]:14} {dragonColor[id]:8} {dragonType[id]:14} {riderFname[id]:14} {riderLname[id]:14}")

def riderSearch(name, list):
     #searchTerm is local var name and only exist in this def block
    ids = search(name,list)
    if ids == 0:
        print("**INVALID CONGRATS**")
    else:
        print("----------------------------------------------------------------------------------------------------------------\n")
        print(f"{'DRAGON NAME':14} {'PRONOUNCIATION':16} {'NICK NAME':10} {'MEANING':14} {'COLOR':8} {'TYPE':14} {'RIDER FNAME':14} {'RIDER LNAME':10}")
        for id in ids:
            print(f"{dragonName[id]:14} {namePronounce[id]:16} {nickName[id]:10} {meaning[id]:14} {dragonColor[id]:8} {dragonType[id]:14} {riderFname[id]:14} {riderLname[id]:14}")
    
    
def search(identifier, list):
    #SEQUENTIAL SEARCH - "in sequence" -> start @ the beggining (0) go to the end (len(listName))
    ids = []
    for i in range(0, len(list)):
        #look at eatch value in a list to find what your looking for
        if list[i] == identifier.capitalize(): #hopefully works to cap. first letter and stop error from running when using lowercase, it works
            ids.append(i)
    if ids == []:
        return 0
    return ids

def clear():
    system('cls')

#---- MAIN CODE ----
dragonName = []
namePronounce = []
nickName = []
meaning = []
dragonColor = []
dragonType = [] 
riderFname = []
riderLname = []
#---- IMPORT CSV ---- 
import csv
from os import system, name

with open("midtermIndividual/dragon.csv") as csvFile:
    #Reade from File
    
    file = csv.reader(csvFile)

    for rec in file:
        dragonName.append(rec[0])
        namePronounce.append(rec[1])
        nickName.append(rec[2])
        meaning.append(rec[3])
        dragonColor.append(rec[4])
        dragonType.append(rec[5])
        riderFname.append(rec[6])
        riderLname.append(rec[7])
      
#---- Disconect from csv ----

#menu has built in header so that the user always sees the name of the program when the menu is shown 
#IMPORTANT(kinda) -> Violet should only show up once when asking for the list of riders but show up twice on the rest of the selections

menuChoice = ""
while menuChoice != 7: # 7 is exit
    menuChoice = menu()
    if menuChoice == 1:
        name = input("Enter Dragon Name: ")
        dragonSearch(name)
        
        input("\nPress enter to continue...")
        
        clear() #Will clear all previous info then move on 

    elif menuChoice == 2:
        color = input("Enter Dragon Color: ")
        dragonColorSearch(color)
        
        input("\nPress enter to continue...")
        
        clear() 

    elif menuChoice == 3:
        type = input("Enter Dragon type: ")
        dragonTypeSearch(type)
        
        input("\nPress enter to continue...")
        
        clear() 

    elif menuChoice == 4:
        #name = input("Enter the name of the Rider: ")
        check = ""
        while check != "F" and check != "L":
            check = input("Would you like to search by [F]irst or [L]ast name: ").upper()
        name = input("Input the name: ")
        if check == "F":
            riderSearch(name, riderFname)
            
            input("\nPress enter to continue...")
            
            clear()
        else:
            riderSearch(name, riderLname)
            
            input("\nPress enter to continue...")
            
            clear()

    elif menuChoice == 5:
        print("---------------------------------------------------") # -- just for seperation 
        print("\t  ---| Showing Dragon Names |---") # -- Dragon names are in rec[0]
        print("---------------------------------------------------")
        for name in dragonName:
            print (f"\t\t{name}")
        
        input("\nPress enter to continue...")
        
        clear()

    elif menuChoice == 6:
        print("---------------------------------------------------")
        print("\t  ---| Showing Rider Names |---") # -- Rider names are in rec[6] for first and rec[7] for last
        print("---------------------------------------------------")
        temp = [] # -- run in temp to stop Violrt form printing twice
        for i in range(0, len(riderFname)):
            name = f"{riderFname[i]} {riderLname[i]}"
            if(name not in temp):
                print(f"\t\t{riderFname[i]} {riderLname[i]}")
                temp.append(name)
        
        input("\nPress enter to continue...")
        
        clear()
    else:
        print("-------------------------------------------------------------------------------")
        print("    | Thank you for useing the: Basgiath War College Dragon Encyclopedia |")
        print("-------------------------------------------------------------------------------")



#***WARNING 6 HOURS WORTH OF MENTAL ANGUISH WENT INTO THIS PLZ BE NICE***