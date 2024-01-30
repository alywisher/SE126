#Allison Wisher
#lab4b -> in class
#1/30/24
#prompt -> [1]Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file. [2]Next, reprocess the lists to find each student's current average score along with the class average.  While processing in the for loop, store each student's average into a new list called 'avg' and reprint the records to include this numeric average.  Reprocess the lists one final time to find the letter equivalent of each student's average and store this into a new list called 'let_avg'.  Reprint the lists for a third time, record by record including average score and average letter equivalent.  After this third print of the original file data, print to the console the total number of student's in the class along with the class numeric average.[3]After your final display using the 1D parallel lists, create one new, empty list, that will become a 2D list.  Then, using a for loop and the 1D parallel lists, store the data to the 2D list you have created. Each index in the 2D list should contain a list of data. This list of data should contain the fname, lname, test1, test2, test3, num_average, and letter_average for the respective student.

#---- MAIN CODE ----

import csv

#creat 1D lists [will be parrele to eatch other] 
#base lists on the feilds in file 

fName = []
lName = []
test1 = []
test2 = []
test3 = []

#connect with the file & read data into 1D list

with open("week4/hw/listPractice1.txt") as csvFile:

    file = csv.reader(csvFile)

    #come back and show print(file) later
    for rec in file:
        # store data from file fields to their respective lists
        #by parellel - storing initial file record data at the same posistion (index) in eatch list --> use the same [index] across each list to find "matching" data
        fName.append(rec[0])
        lName.append(rec[1])
        test1.append(int(rec[2])) #cast as an int for math
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#---- disconnect from file ----
        
#---- PROCESS THE LIST --> for loop ----
        
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'}")
print("--------------------------------------------------------------------")

for i in range(0, len(fName)):
    #len() --> returns length of (item) -> for lists, it is the # of the items in the list

    print(f"{fName[i]:12} \t {lName[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")


#calculate and stro\e eatch students AVRAGE TEST SCORE

avg = 0
totalCount = 0 
#creat the list
average = []

for i in range(0, len(test1)):

    #calculate avg for student
    avg = (test1[i] + test2[i] + test3[i]) / 3
    #append this avg to the avrage[]
    average.append(avg)

#---- Display studens fName and avg test grade ----
    
print(f"{'FIRST'} \t {'AVERAGE'}")
for i in range(0, len(fName)):

    print(f"{fName[i]:12} \t {average[i]:8.1f}")

#SEQUENTIAL SEARCH : "in sequence" --> from beging through the end
lowName = ""
lowAvg = 100 #start with highest value to drop to find the lowest

for i in range(0, len(average)):
    #determin if the current average is lower than the current lowAvg
    if average[i] < lowAvg:
        lowAvg = average[i] #current average is lower, so becomes new low value
        lowName = fName[i]

#---- DISPLAY: total students in file ----\
print(f"STUDENTS IN FILE: {len(fName)}")
print(f"LOWEST AVERAGE: {lowName} - {lowAvg:.1f}")

#---- 2D lists ------------------------------------------------------------------------------------------------------------------------------

#use your 1D list to populate a new 2D list
#HINT: the 2D lists is a list ... populated with lists 8D

allStudents = []

for i in range(0, len(fName)):
    #add eatch students data to their [index] place in the allStudents list[]
    allStudents.append([fName[i], lName[i], test1[i], test2[i], test3[i], average[i]])

#---- Display the 2D list to the consol - for now, just get them the lists to display ie ['Floyd','Eastham','100','85','93']
for i in range(0, len(allStudents)):
    print(f"{allStudents[i]}")

print(f"---- 2D - lists - INDIV. - VALUES ----")
print(f"{'FIRST':10}\t{'LAST':12}\t{'TEST1':7}\t{'TEST2':7}\t{'TEST3':7}\t{'AVERAGE':7}\t{'LETTER GRADE'}")
print("------------------------------------------------------------------------------------------------------")

#display the 2D list to the console where eatch value list apears as a value (not a list item)

for i in range(0, len(allStudents)):
    #we have lists within lists - outer for handles main list (allStudents)
    if allStudents[i][5] > 90:
        allStudents[i].append("\t\t\t\tA")
    elif allStudents[i][5] > 80:
        allStudents[i].append("\t\t\t\tB")
    elif allStudents[i][5] > 70:
        allStudents[i].append("\t\t\t\tC")
    elif allStudents[i][5] > 60:
        allStudents[i].append("\t\t\t\tD")
    else:
        allStudents[i].append("\t\t\t\tF")


    for x in range(0, len(allStudents[i])):
        #inner for handles each value found at current list (allStudents[i])
        if type(allStudents[i][x]) == str:
            print(f"{allStudents[i][x]:10}", end="\t")
        else:
            print(f"{allStudents[i][x]:7.1f}", end="\t")

 

    #include an extra empty print() to cancel the interior print's end=""
    print()





