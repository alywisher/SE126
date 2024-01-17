#W2D2 - Text file opening review + 1D List

import csv

totalRecords = 0

fNames = []
lNames = []
faveNums = []
faveAnimals = []

with open("week2/demo/w2d2_demoTextFile.txt") as textfile:
    #with colens you must indent when connected to & reading the file 

    file = csv.reader(textfile)

    for rec in file: 
        # for every record found in file (entire row in field data)

        print('rec')

        #appemd field for the records
        fNames.append(rec[0]) 
        lNames.append(rec[1])
        faveNums.append(int(rec[2]))

        #len() --> returns length of a structure (list);
        #the maximum length of rec is: 4 

        if len(rec) == 4: 

            faveAnimals.append(rec[3])
        else:
            #rec[3] does not exist  
            faveAnimals.append("---")

#process fNames + feaveAnimals list to display
            
for index in range(0, len(fNames)): 
    print(f"{fNames[index]}'s fave animal is {faveAnimals[index]}")




