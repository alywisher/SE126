import csv

#creat 1D lists [will be parrele to eatch other] 
#base lists on the feilds in file 

fName = []
lName = []
test1 = []
test2 = []
test3 = []

#connect with the file & read data into 1D list

with open("week4/demo/listPractice1-1.txt") as csvFile:

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
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'}")
print("--------------------------------------------------------------------")

#display the 2D list to the console where eatch value list apears as a value (not a list item)
for i in range(0, len(allStudents[1])):
    #we have lists within lists - outer for handles main list (allStudents)
    for x in range(0, len(allStudents[i])):
        #inner for handles each value found at current list (allStudents[i])
        print(f"{allStudents[i][x]}", end="")


    #include an extra empty print() to cancel the interior print's end=""
    print()


