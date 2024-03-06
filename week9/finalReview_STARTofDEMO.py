#WEEK 9: FINAL REVIEW

#This review demo will cover all major topics from SE126.  It utilizes: 'finalReview_text.txt'
#Documentation has been added post demo to enhance understandig of the code

#in this review program, you will:
#   1 - connect to a file and import its data into lists
#               1a - the lists are UNEVEN so a filter system must be used
#               1b - count the total number of people in the file
#   2 - process the lists to print the original data to the console
#   3 - process the lists to find:
#               3a - the youngest person in the list
#               3b - the oldest person in the list
#               3c - the average age of the people in the list
#   4 - a search option to search for id codes within the list
#           ** utilize menu '1. Sequential 2. Binary 3. Exit' that is printed from a function that returns the user's selection choice
#               4A - allow user to search multiple time
#               4a - sequential search will be performed w/ output to visualize search
#               4b - binary search will be performed w/ output to visualize search

#FUNCITONS-----------------------------------------------------------------------
def hello():

    print("Welcome to the SE126 FINAL REVIEW!")

def goodbye():

    print("Thank you for viewing the review. Now GO STUDY and kick some Finals butt!")


#a function that swaps values for bubble sorting

def swap(listName, posi): 
    #posi -> current position (index) of where swap needs to accur
    temp = listName[posi]
    listName[posi] = listName[posi + 1]
    listName[posi + 1] = temp

    #this function could not return OR return TWO values ...
    #return nothing: because list are stored to memory for the program; when we swap value places, list is automatically updated

    #python supports multi return values
    #return listName[posi], listName[posi + 1]
    #in main code, the call looks like this : 
    #                                        firstName[j], firstName[j + 1] = swap(firstName, j)

#a function that allows a user to search by sequential search or binary search
def search_menu():

    menuOptions = [1, 2, 3]

    print("1. Sequential Search")
    print("2. Binary Search")
    print("3. Exit")

    try:
        response = int(input("Please enter your choice [1 - 3]: "))
    except:
        print("INVALID!")
        return search_menu()
   
    while response not in menuOptions:

        print("*ERROR*ERROR*")
        response = int(input("Please enter your choice [1 - 3]: "))

    #this function should return the user's selection AFTER checking that it is a valid input()
    return response


#---------------------------------------------------------------------------------
import csv

hello()


num_rec = 0

#create empty lists in order to store file data
idCode = []
lastName = []
firstName = []
age = []
allegiance = []
num = [] #if == 1, no color2 value ... only when == 2 is there a color2 value
color1 = []
color2 = [] #only when num (rec[5] from file) is == 2 is there a color2 present

#1 - connect to a file and import its data into lists
with open("week9/txtFiles/finalReview_text.csv") as csvfile:

    file = csv.reader(csvfile)

    #when reading files, each record is treated as a list
    #each field of data (rec[#]) represents a new value
    for rec in file:

        #this for loop will run for as many records (rows) of data in the file

        #store data into lists --> .append()
        idCode.append(rec[0])
        lastName.append(rec[1])
        firstName.append(rec[2])
        age.append(int(rec[3]))
        allegiance.append(rec[4])
        num.append(rec[5])
        color1.append(rec[6])

        #1a - the lists are UNEVEN so a filter system must be used
        #(not all records in the file have a color2, so we must filter)

        if rec[5] == "2":
            color2.append(rec[7])
        elif rec[5] == "1":
            color2.append("-none-")
        else:
            color2.append("ERROR!")

        #1b - count the total number of people in the file
        #add one to total number of records, necessary for for loop processing
        num_rec += 1 

print("Finished storing data from file. Disconnecting from file now.\n\n")


#   2 - process the lists to print the original data to the console
print("-----------------ORIGINAL FILE DATA-----------------------------------------------------------------------------------")
print(f"{'idCode':10}\t{'lastName':15}\t{'firstName':15}\t{'age':3}\t{'allegiance':35}\t{'num':3}\t{'color1':7}\t{'color2':7}")
print("----------------------------------------------------------------------------------------------------------------------")
for i in range(0, num_rec):

    #the for loop will start with 'i = 0'
    #for loop will +1 to value of 'i' through each pass through the loop
    #for loop will run for 'num_rec' times (for each record in the list)
    #wherever 'i' is present, replace with current loop integer value

    print(f"{idCode[i]:10}\t{lastName[i]:15}\t{firstName[i]:15}\t{age[i]:3}\t{allegiance[i]:35}\t{num[i]:3}\t{color1[i]:7}\t{color2[i]:7}")




#   3 - process the lists to find:
#PROCESS = FOR LOOP! for loops were BUILT for list/array processing!

#Ask yourself: 
#If the AGE list were ordered in *increasing numeric* order, 
#where would you find:
# [0]                   - the youngest person in the list
# [len(age) - 1]        - the oldest person in the list

#sort the list by increasing order 
#BUBBLE SORT
for i in range(0, len(age) - 1):
    for j in range(0, len(age) - 1):
        if age[j] > age[j + 1]:

            #SWAP VALUES: 
            ageSwap = age[j]
            age[j] = age[j + 1]
            age[j + 1] = ageSwap

            swap(firstName, j)
            swap(lastName, j)
            swap(idCode, j)
            swap(allegiance, j)
            swap(color1, j)
            swap(color2, j)
            swap(num, j)

totalAge = 0
for i in range(0, num_rec):
    #print(f"{idCode[i]:10}\t{lastName[i]:15}\t{firstName[i]:15}\t{age[i]:3}\t{allegiance[i]:35}\t{num[i]:3}\t{color1[i]:7}\t{color2[i]:7}")
    totalAge += age[i]


#Ask yourself:
#What do you need to find an average? 
#               3c - the average age of the people in the list
avgAge = totalAge / len(age)

oldAge = age[len(age) - 1]
oldFName = firstName[len(age) - 1]

youngAge = age[0]
youngFName = firstName[0]

print(f"\n\n---HERE IS SOME NEW DATA:")
print(f"\t\t          Oldest person: {oldFName} is {oldAge}yrs old")
print(f"\t\t    Youngest person: {youngFName} is {youngAge}yrs old")
print(f"Average age in file: {avgAge:.1f}yrs old\n\n")
#for i in range(0, num_rec):

    




#avg_age = #calculate average age









#   4 - a search option to search for id codes within the list
#           ** utilize menu '1. Sequential 2. Binary 3. Exit' that is printed from a function that returns the user's selection choice
#4A - allow user to search multiple time
#if the function has a RETURN we must store its return to use in our base program

answer = "y" #allows us to get in loop

while answer == "y":

    #call menu function so we have options from menu -- this function will be returning the user's selection and storing it into the var userChoice
    userChoice = search_menu

    if userChoice == 1:
        #4a - sequential search will be performed w/ output to visualize search
        print("sequential search")
        #ask for search query
        search = input("\n\tWhich Last Name are you looking for:")
        #we could also search for alligent, nums, color1, color2, (all non-unique)
        
        #create an empty list to store items
        found = []

        #run sequential search
        for i in range(0, len(lastName)):
            if search.lower() == lastName[i].lower():
                #found somone!
                found.append(i) #remember: found is a list of index #'s aka locations
        
        #print results
        if not found:
            print(f"\n\tSorry we could not find: {search}")
        else:
            print(f"\n\tHere is what we found for {search}: ")
            for i in range(0, len(found)):
                print(f"{idCode[found[i]]:10}\t{lastName[found[i]].upper():15}\t{firstName[found[i]]:15}\t{age[found[i]]:3}\t{allegiance[found[i]]:35}\t{num[found[i]]:3}\t{color1[found[i]]:7}\t{color2[found[i]]:7}")


    if userChoice == 2:

        print("Binery search")
        #4b - binary search will be performed w/ output to visualize search
        #BINARY SEARCH CAN ONLY BE USED ON ORDERED LISTS

        #ask for search query
        search = input("Which first name are you looking for: ")

        #sort list & linked data
        for i in range(0, len(firstName) - 1):
            for j in range(0, len(firstName) - 1):
                if firstName[j] > firstName[j + 1]:
                    #swap places
                    swap(firstName, j)
                    swap(lastName, j)
                    swap(idCode, j)
                    swap(allegiance, j)
                    swap(color1, j)
                    swap(color2, j)
                    swap(num, j)

        #binary search list
        min = 0
        max = len(firstName) - 1
        mid = int((min + max) / 2)

        while min < max and search != firstName[mid]:
            if search > firstName[mid]:
                min = mid + 1
            else:
                max = mid - 1
            mid = int((min + max) / 2)
        #print results
        if search == firstName[mid]:
            print(f"\n\tYAY! We found your search for {search}!")
            print(f"{idCode[mid]:10}\t{lastName[mid].upper():15}\t{firstName[mid]:15}\t{age[mid]:3}\t{allegiance[mid]:35}\t{num[mid]:3}\t{color1[mid]:7}\t{color2[mid]:7}")
        else:
            print(f"womp womp, could not find {search} :[")


    if userChoice == 3: 
        print("exit")
        #EXIT PROGRAM
        answer = "x"



    #which menu choices do NOT want to be asked if they want to run again?
    if userChoice in [1, 2]:

        answer = input("\nWould you like to see the menu again [y/n]:").lower()

goodbye()